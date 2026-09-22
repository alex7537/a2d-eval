"""Publish an opted-in terminal report without touching the working checkout."""
import argparse,hashlib,json,os,shutil,subprocess,tempfile,time
from pathlib import Path
FILES=('index.html','app.js','style.css','results.json','REPORT.md')
def merge(existing,incoming):
    batches={r['batch'] for r in incoming['runs']}
    result=dict(existing)
    result['runs']=[r for r in existing.get('runs',[]) if r['batch'] not in batches]+incoming['runs']
    result['generated_at']=incoming['generated_at']
    return result

def publish(batch,remote,branch='main'):
    batch=Path(batch);site=batch/'static_report'
    def git(path,*args):
        return subprocess.check_output(['git','-C',str(path),*args],stderr=subprocess.STDOUT,text=True,timeout=120,env=dict(os.environ,GIT_TERMINAL_PROMPT='0',GIT_SSH_COMMAND='ssh -o BatchMode=yes -o ConnectTimeout=15')).strip()
    incoming=json.loads((site/'results.json').read_text())
    if any(r['state'] not in ['已完成','暂停','异常停止／未完成','采集结束／等待确认'] for r in incoming['runs']):raise ValueError('Only terminal reports can be published')
    for attempt in range(3):
        try:
            with tempfile.TemporaryDirectory(prefix='a2d-publish-') as tmp:
                git(tmp,'clone','--depth','1','--branch',branch,remote,'repo');repo=Path(tmp)/'repo'
                dest=repo/'reports'/batch.name;dest.mkdir(parents=True,exist_ok=True)
                for name in FILES:shutil.copyfile(site/name,dest/name)
                latest=repo/'reports/latest';latest.mkdir(parents=True,exist_ok=True)
                old=json.loads((latest/'results.json').read_text()) if (latest/'results.json').exists() else {}
                payload=merge(old,incoming);raw=json.dumps(payload,ensure_ascii=False,indent=2)+'\n';(latest/'results.json').write_text(raw)
                if not (latest/'index.html').exists():
                    for name in ['index.html','app.js','style.css']:shutil.copyfile(site/name,latest/name)
                mf=latest/'manifest.json';manifest=json.loads(mf.read_text()) if mf.exists() else {}
                groups=[g for r in payload['runs'] for g in r['groups']]
                manifest.update(generated_at=payload['generated_at'],runs=len(payload['runs']),groups=len(groups),attempts=sum(g['attempts'] for g in groups),results_sha256=hashlib.sha256(raw.encode()).hexdigest())
                mf.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
                git(repo,'add','reports/'+batch.name,'reports/latest')
                if git(repo,'diff','--cached','--name-only'):
                    git(repo,'-c','user.name=A2D report publisher','-c','user.email=149937165+alex7537@users.noreply.github.com','commit','-m','Archive evaluation '+batch.name)
                    git(repo,'push','origin','HEAD:refs/heads/'+branch)
                sha=git(repo,'rev-parse','HEAD')
                if git(repo,'ls-remote','origin','refs/heads/'+branch).split()[0]!=sha:raise RuntimeError('Remote advanced; retry merge')
                result=dict(state='published',commit=sha,remote=remote,branch=branch,time=time.time());break
        except Exception as e:
            result=dict(state='failed',error=str(e),remote=remote,branch=branch,time=time.time(),attempts=attempt+1)
    temp=batch/'publish_status.json.tmp';temp.write_text(json.dumps(result,ensure_ascii=False,indent=2));temp.replace(batch/'publish_status.json')
    return result
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--batch',required=True);ap.add_argument('--remote',required=True);ap.add_argument('--branch',default='main');a=ap.parse_args()
    r=publish(a.batch,a.remote,a.branch);print(json.dumps(r,ensure_ascii=False));raise SystemExit(0 if r['state']=='published' else 1)
