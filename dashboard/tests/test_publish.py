import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from publish_report import merge
class PublishTests(unittest.TestCase):
 def test_merge_preserves_other_batches_and_training(self):
  old={'runs':[{'batch':'a','old':True},{'batch':'b'}],'training_runs':[1]}
  new={'runs':[{'batch':'a','new':True}],'generated_at':'now'}
  result=merge(old,new)
  self.assertEqual(result['runs'],[{'batch':'b'},{'batch':'a','new':True}]);self.assertEqual(result['training_runs'],[1]);self.assertEqual(merge(result,new),result)
