import copy
import unittest
from dashboard.compare_training_lifecycle import lifecycle

class LifecycleTest(unittest.TestCase):
    def setUp(self):
        self.snapshot = {"project": "team/project", "generated_at": "old", "runs": [
            {"wandb_run_id": "a", "state": "running", "progress": 0.1},
            {"wandb_run_id": "b", "state": "finished"}]}

    def test_polling_metrics_and_order_do_not_trigger(self):
        other = copy.deepcopy(self.snapshot)
        other["generated_at"] = "new"
        other["runs"][0].update(progress=0.8, updated_at="new", latest_metrics={"loss": 0.2})
        other["runs"].reverse()
        self.assertEqual(lifecycle(self.snapshot), lifecycle(other))

    def test_lifecycle_and_membership_changes_trigger(self):
        for state in ["finished", "failed", "crashed", "killed"]:
            other = copy.deepcopy(self.snapshot)
            other["runs"][0]["state"] = state
            self.assertNotEqual(lifecycle(self.snapshot), lifecycle(other))
        other = copy.deepcopy(self.snapshot)
        other["runs"].append({"wandb_run_id": "c", "state": "running"})
        self.assertNotEqual(lifecycle(self.snapshot), lifecycle(other))
        other["runs"] = []
        self.assertNotEqual(lifecycle(self.snapshot), lifecycle(other))

    def test_invalid_identity_fails(self):
        self.snapshot["runs"].append(self.snapshot["runs"][0])
        with self.assertRaises(ValueError):
            lifecycle(self.snapshot)
