"""Export the canonical auto-report snapshot as a standalone static website."""
import argparse, json, shutil
from pathlib import Path

STATIC = Path(__file__).parent / 'static'

def export_report(batch, output):
    batch, output = Path(batch), Path(output)
    status = json.loads((batch/'auto_report_status.json').read_text())
    runs=[]
    for row in status['rows']:
        scene=row['scene']; plan=json.loads((batch/scene/'plan.json').read_text())
        model=row['model']; valid=row['valid']
        group=dict(row, label=model, mode='report', method=' / '.join(plan.get('modes',['step_gt'])),
                   planned=plan.get('episodes_per_configuration'), rate=row['successes']/valid if valid else None,
                   failures=row['failure_observations'], failure_source='与 AUTO_REPORT.md 同一次汇总',
                   training_data=plan.get('training_data','待核实'), training_data_source='冻结 plan.json；缺失不推断',
                   sha256=plan.get('expected_hashes',{}).get(model))
        runs.append(dict(id=f'{batch.name}/{scene}/{model}',batch=batch.name,scene=scene,state=status['state'],
                         groups=[group],warnings=status['warnings'],updated_at=status['updated_at'],
                         protocol=dict(horizon=plan.get('horizon'),max_steps=plan.get('max_steps'),policy_seed=plan.get('policy_seed'),
                                       metric=plan.get('metric','未记录'),layout_replay=plan.get('layout_replay',False),
                                       limitations=['静态归档；执行模式按原报告汇总，不代表逐模式对照'])))
    output.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(STATIC/'evaluation.html',output/'index.html')
    for name in ('evaluation.html','app.js','style.css'):shutil.copyfile(STATIC/name,output/name)
    html=(output/'index.html').read_text().replace('href="/style.css"','href="./style.css"').replace('src="/app.js"','src="./app.js"').replace('href="/evaluation.html"','href="./index.html"').replace('href="/"','href="./index.html"')
    html=html.replace('<script src="./app.js">','<script>window.STATIC_REPORT=true;</script><script src="./app.js">')
    (output/'index.html').write_text(html)
    payload=dict(generated_at=status['updated_at'],runs=runs,scope='静态结果快照 · 与随附报告一致')
    temp=output/'results.json.tmp';temp.write_text(json.dumps(payload,ensure_ascii=False,indent=2));temp.replace(output/'results.json')
    shutil.copyfile(batch/'AUTO_REPORT.md',output/'REPORT.md')
    return output

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--batch',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();print(export_report(args.batch,args.output))
