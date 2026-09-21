import json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from export_report import export_report
from export_dashboard import export_from_snapshot
class ExportTest(unittest.TestCase):
 def test_report_counts_and_relative_assets(self):
  with tempfile.TemporaryDirectory() as tmp:
   batch=Path(tmp)/'batch';(batch/'box').mkdir(parents=True)
   (batch/'box/plan.json').write_text(json.dumps({'episodes_per_configuration':3,'models':{'dp':'x'}}))
   (batch/'AUTO_REPORT.md').write_text('canonical report')
   (batch/'auto_report_status.json').write_text(json.dumps(dict(rows=[dict(scene='box',model='dp',valid=2,successes=1,attempts=3,invalid=1,failure_observations={'unknown':1})],state='已完成',warnings=[],updated_at='now')))
   out=export_report(batch,Path(tmp)/'site');g=json.loads((out/'results.json').read_text())['runs'][0]['groups'][0]
   self.assertEqual((g['successes'],g['valid'],g['invalid'],g['rate']),(1,2,1,.5))
   self.assertIn('./app.js',(out/'index.html').read_text());self.assertEqual((out/'REPORT.md').read_text(),'canonical report')
 def test_refresh_static_snapshot_with_training_links(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);source=root/'evaluation.json';out=root/'site'
   source.write_text(json.dumps(dict(generated_at='old',scope='old',runs=[dict(batch='b',scene='box',groups=[dict(model='m',mode='x',sha256='abc',attempts=2,successes=1,valid=2,invalid=0,rate=.5,method='x')])])) )
   data=export_from_snapshot(source,out)
   self.assertIn('training',data);self.assertTrue((out/'results.json').is_file());self.assertIn('training_runs',json.loads((out/'manifest.json').read_text()))
