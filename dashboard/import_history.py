"""Import canonical historical summaries and audited later ledgers, without handoff duplicates."""
import argparse,json,hashlib,re
from pathlib import Path

def build(source,catalog):
 runs=[];audit=[]
 def emit(p,batch,model,scene,n,valid,s,metric,rt,fail,bundle=None,basis='',extra=None):
  assert 0<=s<=valid<=n,(p,s,valid,n)
  g=dict(model=model,label=model,mode='history',method='历史协议',training_data='待核实',training_data_source='历史训练集未重新审计',attempts=n,planned=None,valid=valid,successes=s,invalid=n-valid,rate=s/valid if valid else None,failures=fail,failure_source='原记录诊断标签；未重算物理信号',bundle=bundle,denominator_basis=basis)
  if sum(fail.values())!=valid-s:g['failures']={'未完成该指标（原因未审计）':valid-s} if valid>s else {}
  runs.append(dict(id=str(p),batch=batch,scene=scene,state='历史归档',groups=[g],warnings=['历史快照可能与相邻版本重叠，不跨批累加；'+basis],protocol=dict(horizon=rt.get('execute_horizon'),max_steps=rt.get('max_steps'),policy_seed=rt.get('base_seed'),metric=metric,layout_replay=False,limitations=['保留原指标，不能与当前抓取成功率直接排名']),updated_at=None,historical=True,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),additional_metrics=extra or {}))
 for p in sorted(source.glob('*summary.json')):
  d=json.loads(p.read_text());n=d.get('completed');s=d.get('funnel_counts',{}).get('success',d.get('successes'))
  if not isinstance(n,int) or not isinstance(s,int):audit.append(dict(file=str(p),status='仅索引：缺少成功或完成计数'));continue
  stage=dict(d.get('failure_stage_counts',d.get('failure_counts',{})));excluded=sum(v for k,v in stage.items() if k in ['runtime_error','reset_invalid'] and isinstance(v,int));fail={k:v for k,v in stage.items() if k not in ['runtime_error','reset_invalid'] and isinstance(v,int)}
  version=re.search(r'_v(\d+)_',p.name);v=version.group(1) if version else '1' if p.name.startswith('a2d_hand_funnel_') else None
  criterion=d.get('criterion',{});metric=criterion.get('success') if isinstance(criterion,dict) else str(criterion)
  if not metric:
   metric=next((str(value) for k,value in d.items() if k.endswith('_criterion')),None) or '最大抬升≥1cm（原报告指标）'
  batch='共享历史 v'+v if v else '共享历史专项 · '+p.stem.replace('_summary','')
  model=d.get('configuration',d.get('model')) or p.stem
  emit(p,batch,model,'历史场景（未重新核验）',n,n-excluded,s,metric,d.get('fixed_runtime',{}),fail,d.get('bundle'),'summary completed减显式runtime_error/reset_invalid；未重审未标注的初态异常',d.get('funnel_counts',{}))
  audit.append(dict(file=str(p),status='已接入',raw=n,valid=n-excluded,success=s))
 for entry in catalog['later_jsonl']:
  p=Path(entry['file']);rr=[json.loads(l) for l in p.read_text().splitlines() if l.strip()]
  noerr=[r for r in rr if not(r.get('error_type') or r.get('error_message') or r.get('error') or r.get('failure_stage')=='runtime_error')]
  height=all(isinstance(r.get('initial_z_m'),(int,float)) for r in noerr)
  good=[r for r in noerr if not r.get('reset_invalid') and r.get('reset_valid',True) and (r.get('initial_z_m',0)>=.4 if height else True)]
  success=sum(bool(r.get('grasp_lift_5cm',r.get('success'))) for r in good)
  emit(p,entry['batch'],entry['model'],entry['scene'],len(rr),len(good),success,'多指接触＋抬升≥5cm；原逐轮grasp_lift_5cm字段',{}, {},entry.get('bundle'),'逐轮排除运行异常及显式reset异常'+('，initial_z≥0.4m' if height else '；缺少高度，未进行高度筛查'),{'success10':sum(bool(r.get('grasp_lift_10cm')) for r in good)})
  audit.append(dict(file=str(p),status='已重算接入',raw=len(rr),valid=len(good),success=success))
 return runs,audit
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--catalog',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();runs,audit=build(a.source,json.loads(a.catalog.read_text()));a.output.write_text(json.dumps(runs,ensure_ascii=False,indent=2)+'\n');a.output.with_name('history_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n');print('imported',len(runs),'indexed',len(audit))
