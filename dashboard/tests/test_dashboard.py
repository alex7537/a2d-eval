import sys,json,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from server import aggregate
class DashboardTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.p=Path(self.tmp.name)/'batch'/'box';self.p.mkdir(parents=True)
 def put(self,plan,rows):
  (self.p/'plan.json').write_text(json.dumps(plan));(self.p/'episodes.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in rows))
 def test_denominator_duplicate_and_partial(self):
  a=dict(model='dp_latest',mode='step_gt',episode=0,outcome='completed',success=True)
  self.put(dict(models={'dp_latest':'bundle'},episodes_per_configuration=3),[a,a,dict(a,episode=1,outcome='infrastructure_error',success=False)])
  with (self.p/'episodes.jsonl').open('a') as f:f.write('{')
  r=aggregate(self.p);g=r['groups'][0]
  self.assertEqual((g['attempts'],g['valid'],g['invalid'],g['rate']),(2,1,1,1.));self.assertEqual(len(r['warnings']),2)
 def test_rdt_missing_contact_unknown(self):
  self.put(dict(model='RDT',attempts=10),[dict(episode=0,completed=True,success=False,max_lift=.1)])
  g=aggregate(self.p)['groups'][0];self.assertEqual(g['failures'],{'证据不足，待逐步审计':1})
 def test_audit_and_modes(self):
  self.put(dict(models={'dp_latest':'x'},modes=['step_gt','batch16']),[dict(model='dp_latest',mode='step_gt',episode=0,outcome='completed',success=False,contacts=2,max_lift=.1)])
  audit={('batch','box','dp_latest'):dict(categories={'接触与抬升不同步':1},success_mismatches=[])}
  r=aggregate(self.p,audit);self.assertEqual(r['groups'][0]['failures'],{'接触与抬升不同步':1});self.assertEqual(r['groups'][1]['attempts'],0)
if __name__=='__main__':unittest.main()
