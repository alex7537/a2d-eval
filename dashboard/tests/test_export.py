import json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from export_report import export_report
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
