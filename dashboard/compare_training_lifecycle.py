"""Compare run identities and lifecycle states; ignore metrics and polling times."""
import argparse
import json
from pathlib import Path


def lifecycle(snapshot):
    project = snapshot["project"]
    states = {}
    for run in snapshot["runs"]:
        key = run["wandb_run_id"]
        state = run["state"]
        if not key or not state or key in states:
            raise ValueError("Missing or duplicate run identity/state")
        states[key] = state
    return project, states


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("previous", type=Path)
    parser.add_argument("candidate", type=Path)
    args = parser.parse_args()
    candidate = lifecycle(json.loads(args.candidate.read_text()))
    previous = lifecycle(json.loads(args.previous.read_text())) if args.previous.exists() else None
    print("unchanged" if candidate == previous else "changed")


if __name__ == "__main__":
    main()
