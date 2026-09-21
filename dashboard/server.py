"""Read-only localhost evaluation dashboard. No simulator controls."""
import argparse, collections, datetime, json, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

STATIC = Path(__file__).parent / 'static'
TRAINING_RUNS = Path(__file__).parent / 'training_runs.json'
MODEL_REGISTRY = Path(__file__).parent / 'model_registry.json'
LABELS = {'dp_latest':'DP spatial49','imle_latest':'IMLE spatial49','cfm_latest':'CFM spatial49','cfm_patch49_latest':'CFM spatial49','cfm_cls_latest':'CFM CLS','cfm_pro5000_latest':'CFM PRO5000','wan_latest':'Joint WAM'}
MODES = {'step_gt':'逐步 RPC＋GT','step':'逐步 RPC','batch16':'合并16动作','Step+GT+contact':'逐步 RPC＋GT'}

def read(path, default=None):
    try: return json.loads(path.read_text())
    except (OSError, ValueError): return {} if default is None else default

def ledger(path):
    rows=[]; seen=set(); warnings=[]
    try: lines=path.read_text().splitlines()
    except OSError: return rows,warnings
    for i,line in enumerate(lines,1):
        try: row=json.loads(line)
        except ValueError:
            warnings.append(f'第{i}行未完成或损坏，未计入');continue
        if not isinstance(row,dict): warnings.append(f'第{i}行格式错误');continue
        key=(row.get('model'),row.get('mode'),row.get('episode',row.get('episode_index',i)))
        if key in seen: warnings.append(f'第{i}行重复，未计入');continue
        seen.add(key);rows.append(row)
    return rows,warnings

def classify(r):
    if r.get('success'): return None
    if r.get('outcome')=='policy_rejected': return '预测被保护规则拒绝'
    if 'contacts' in r and r['contacts']==0: return '无有效接触'
    if r.get('max_lift') is not None and r['max_lift']<.05: return '未抬升5cm'
    if 'contacts' not in r: return '证据不足，待逐步审计'
    return '接触/抬升不同步或持续不足'

def aggregate(folder, audit=None):
    plan=read(folder/'plan.json');rows,warnings=ledger(folder/'episodes.jsonl')
    models=plan.get('models') or {plan.get('model','未记录模型'):plan.get('model_bundle','')}
    modes=plan.get('modes') or [plan.get('mode','step_gt')]
    groups=[]
    for model in models:
        for mode in modes:
            rs=[r for r in rows if r.get('model',model)==model and r.get('mode',mode)==mode]
            valid=[r for r in rs if r.get('outcome') in ('completed','policy_rejected') or ('outcome' not in r and r.get('completed') is True)]
            success=sum(r.get('success') is True for r in valid)
            cats=collections.Counter(classify(r) for r in valid if not r.get('success'))
            category_source='回合摘要（诊断现象）'
            errors=collections.Counter()
            for r in rs:
                if r in valid: continue
                error=r.get('error','未记录异常详情')
                if isinstance(error,dict): error=error.get('error',str(error))
                errors[str(error)]+=1
            audited=(audit or {}).get((folder.parent.name,folder.name,model))
            if audited and not audited.get('success_mismatches'):
                ac={k:v for k,v in audited['categories'].items() if k!='成功'}
                if sum(ac.values())==len(valid)-success and audited['categories'].get('成功',0)==success:
                    cats=ac;category_source='逐步数据审计（诊断现象）'
            quota=plan.get('episodes_per_configuration',plan.get('attempts'))
            groups.append(dict(model=model,label=LABELS.get(model,model),mode=mode,method=MODES.get(mode,mode),attempts=len(rs),planned=quota,valid=len(valid),successes=success,invalid=len(rs)-len(valid),rate=success/len(valid) if valid else None,failures=dict(cats),infrastructure_errors=dict(errors),failure_source=category_source,sha256=plan.get('expected_hashes',{}).get(model),bundle=models[model]))
    status=read(folder/'status.json');supervisor=read(folder/'supervisor_status.json')
    state=supervisor.get('state',status.get('state','unknown'))
    quota_complete=all(g['planned'] is not None and g['attempts']>=g['planned'] for g in groups)
    if quota_complete: state='completed'
    elif state in ('running','loading','cuda_loading'):
        pid=status.get('pid') or supervisor.get('client_pid')
        if not pid or not Path('/proc',str(pid)).exists():state='unverified'
    return dict(id=str(folder),batch=folder.parent.name if folder.name in ('box','bottle') else folder.name,scene=plan.get('scene',folder.name),state=state,groups=groups,warnings=warnings,protocol=dict(horizon=plan.get('horizon'),max_steps=plan.get('max_steps'),policy_seed=plan.get('policy_seed'),metric=plan.get('metric','未记录'),layout_replay=plan.get('layout_replay',False),limitations=plan.get('limitations',[])),updated_at=datetime.datetime.fromtimestamp((folder/'episodes.jsonl').stat().st_mtime).astimezone().isoformat(timespec='seconds') if (folder/'episodes.jsonl').exists() else None)

def attach_training_runs(runs, training_path=TRAINING_RUNS, registry_path=MODEL_REGISTRY):
    training=read(Path(training_path),{'runs':[]})
    registry=read(Path(registry_path),{'links':[]})
    records={row.get('wandb_run_id'):dict(row,checkpoints=[]) for row in training.get('runs',[]) if row.get('wandb_run_id')}
    groups=[]
    for run in runs:
        for group in run.get('groups',[]):groups.append((run,group))
    warnings=[]
    for link in registry.get('links',[]):
        record=records.get(link.get('training_run_id'))
        if record is None:
            warnings.append(f"训练run不存在：{link.get('training_run_id')}");continue
        matched=[]
        sha=link.get('bundle_sha256')
        if sha:
            matched.extend((run,group) for run,group in groups if group.get('sha256')==sha)
        allowed_batches=set(link.get('evaluation_batches',[]))
        if allowed_batches:
            matched=[(run,group) for run,group in matched if run.get('batch') in allowed_batches]
        for selector in link.get('evaluation_selectors',[]):
            matched.extend((run,group) for run,group in groups
                           if group.get('model')==selector.get('model')
                           and (not selector.get('batch') or run.get('batch')==selector.get('batch'))
                           and run.get('batch','').startswith(selector.get('batch_prefix','')))
        unique={}
        for run,group in matched:
            key=(run.get('batch'),run.get('scene'),group.get('model'),group.get('mode'))
            unique[key]=(run,group)
        evaluations=[]
        for run,group in unique.values():
            evaluations.append(dict(batch=run.get('batch'),scene=run.get('scene'),updated_at=run.get('updated_at'),
                                    model=group.get('model'),method=group.get('method'),successes=group.get('successes',0),
                                    valid=group.get('valid',0),invalid=group.get('invalid',0),rate=group.get('rate'),
                                    bundle_sha256=group.get('sha256')))
            group['training_run_id']=record['wandb_run_id']
            group['training_run_url']=record.get('url')
            group['checkpoint_role']=link.get('checkpoint_role')
            group['checkpoint_step']=link.get('checkpoint_step')
        evaluations.sort(key=lambda item:(item.get('updated_at') or '',item.get('batch') or ''),reverse=True)
        record['checkpoints'].append(dict(role=link.get('checkpoint_role'),step=link.get('checkpoint_step'),
                                          bundle_sha256=sha,note=link.get('note'),evaluations=evaluations))
    ordered=sorted(records.values(),key=lambda item:item.get('created_at',''),reverse=True)
    return dict(generated_at=training.get('generated_at'),project=training.get('project'),
                project_url=training.get('project_url'),runs=ordered,warnings=warnings)

def snapshot(root):
    audit_rows=read(root/'weekend_eval_20260920/failure_audit.json',[])
    audit={(r['batch'],r['scene'],r['model']):r for r in audit_rows}
    folders=[]
    for name in ['dp_imle_cfm_latest_two_scenes_100each_20260917_214355','four_latest_step_gt_100each_20260916_162515']:
        folders.extend(root/name/s for s in ['box','bottle'] if (root/name/s/'plan.json').exists())
    # Explicit pilot allowlist; never recursively include backup/snapshot directories.
    for pattern in ['rdt_latest_B19_step_gt_*','rdt_latest_B19_retest_*','rdt_box_50_*','rdt_bottle_50_*','rdt_fixed_smoke_*','rdt_fixed_box_50_*','rdt_fixed_bottle_50_*','legacy_init_box_smoke_*','paired_v3_reset_aligned_models_box_*']:
        folders.extend(p for p in root.glob(pattern) if (p/'plan.json').exists() and any((p/n).exists() for n in ['episodes.jsonl','supervisor_status.json','status.json']))
    live=[aggregate(p,audit) for p in sorted(set(folders))]
    for run in live:
        for group in run['groups']:
            known=run['batch'].startswith(('dp_imle_cfm_latest_two_scenes_', 'four_latest_step_gt_', 'rdt_'))
            group['training_data']='混合数据 · Box＋Bottle' if known else '待核实'
            group['training_data_source']='已核对批次模型归档' if known else '未核对训练数据；不按测试场景推断'
    history=read(Path(__file__).parent/'historical_results.json',[])
    runs=live+history
    training=attach_training_runs(runs)
    return dict(generated_at=datetime.datetime.now().astimezone().isoformat(timespec='seconds'),runs=runs,
                training=training,scope='W&B训练快照＋两批主测试、RDT、初始化对照及历史v19；不同协议不合并排名')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--results',type=Path,required=True);ap.add_argument('--port',type=int,default=8765);args=ap.parse_args()
    cache={};lock=threading.Lock()
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            route=urlparse(self.path).path
            if route=='/api/results':
                try:
                    with lock:
                        if time.monotonic()-cache.get('time',-100)>10:
                            cache['data']=json.dumps(snapshot(args.results),ensure_ascii=False).encode();cache['time']=time.monotonic()
                        data=cache['data']
                    kind='application/json; charset=utf-8'
                except Exception:
                    self.send_error(500,'Result aggregation failed');return
            elif route in ('/','/app.js','/style.css'):
                file={'/':'index.html','/app.js':'app.js','/style.css':'style.css'}[route];data=(STATIC/file).read_bytes();kind={'/':'text/html; charset=utf-8','/app.js':'text/javascript; charset=utf-8','/style.css':'text/css; charset=utf-8'}[route]
            else:self.send_error(404);return
            self.send_response(200);self.send_header('Content-Type',kind);self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
        def log_message(self,*a):pass
    print(f'http://127.0.0.1:{args.port}',flush=True)
    ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
if __name__=='__main__':main()
