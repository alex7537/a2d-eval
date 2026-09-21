"""Freeze the same aggregation used by the local dashboard for static deployment."""
import argparse,json,shutil,hashlib
from pathlib import Path
from server import snapshot,STATIC

def export_dashboard(results,output):
    data=snapshot(Path(results));output=Path(output);output.mkdir(parents=True,exist_ok=True)
    for name in ('index.html','app.js','style.css'):shutil.copyfile(STATIC/name,output/name)
    html=(output/'index.html').read_text().replace('href="/style.css"','href="./style.css"').replace('src="/app.js"','src="./app.js"')
    html=html.replace('<script src="./app.js">','<script>window.STATIC_REPORT=true;</script><script src="./app.js">')
    (output/'index.html').write_text(html)
    raw=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    tmp=output/'results.json.tmp';tmp.write_text(raw);tmp.replace(output/'results.json')
    groups=[g for r in data['runs'] for g in r['groups']]
    manifest=dict(generated_at=data['generated_at'],runs=len(data['runs']),groups=len(groups),attempts=sum(g['attempts'] for g in groups),results_sha256=hashlib.sha256(raw.encode()).hexdigest(),scope=data['scope'])
    (output/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    return data

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--results',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    export_dashboard(a.results,a.output)
