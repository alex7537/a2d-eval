"""Freeze evaluation plus W&B training metadata for static deployment."""
import argparse,json,shutil,hashlib,datetime
from pathlib import Path
from server import snapshot,attach_training_runs,STATIC

def write_dashboard(data,output):
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    for name in ('index.html','evaluation.html','app.js','style.css'):shutil.copyfile(STATIC/name,output/name)
    for name in ('index.html','evaluation.html'):
        path=output/name;html=path.read_text().replace('href="/style.css"','href="./style.css"').replace('src="/app.js"','src="./app.js"').replace('href="/evaluation.html"','href="./evaluation.html"').replace('href="/"','href="./index.html"')
        html=html.replace('<script src="./app.js">','<script>window.STATIC_REPORT=true;</script><script src="./app.js">')
        path.write_text(html)
    raw=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    tmp=output/'results.json.tmp';tmp.write_text(raw);tmp.replace(output/'results.json')
    groups=[g for r in data['runs'] for g in r['groups']]
    training=data.get('training',{}).get('runs',[])
    linked=sum(bool(run.get('checkpoints')) for run in training)
    manifest=dict(generated_at=data['generated_at'],runs=len(data['runs']),groups=len(groups),attempts=sum(g['attempts'] for g in groups),
                  training_runs=len(training),linked_training_runs=linked,training_snapshot_at=data.get('training',{}).get('generated_at'),
                  results_sha256=hashlib.sha256(raw.encode()).hexdigest(),scope=data['scope'])
    (output/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    return data

def export_dashboard(results,output):
    return write_dashboard(snapshot(Path(results)),output)

def export_from_snapshot(evaluation_snapshot,output):
    data=json.loads(Path(evaluation_snapshot).read_text())
    data['generated_at']=datetime.datetime.now().astimezone().isoformat(timespec='seconds')
    data['training']=attach_training_runs(data.get('runs',[]))
    data['scope']='W&B训练快照＋已发布测评快照；不同协议不合并排名'
    return write_dashboard(data,output)

if __name__=='__main__':
    ap=argparse.ArgumentParser();source=ap.add_mutually_exclusive_group(required=True);source.add_argument('--results',type=Path);source.add_argument('--evaluation-snapshot',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    export_dashboard(a.results,a.output) if a.results else export_from_snapshot(a.evaluation_snapshot,a.output)
