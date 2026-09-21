"""Export a privacy-safe, read-only W&B project snapshot for the dashboard."""

from __future__ import annotations

import argparse
import datetime
import json
from pathlib import Path
from typing import Any


def nested(value: dict[str, Any], *keys: str) -> Any:
    current: Any = value
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def first(mapping: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        value = mapping.get(key)
        if value is not None:
            return value
    return None


def number(value: Any) -> float | int | None:
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (int, float)):
        return value
    return None


def policy_name(config: dict[str, Any], summary: dict[str, Any], run_name: str) -> str:
    value = nested(config, "policy", "type") or summary.get("policy_type")
    if value:
        return str(value)
    if run_name.startswith("rdt"):
        return "rdt_170m_a2d"
    if run_name.startswith("dp_") or "diffusion" in run_name:
        return "diffusion"
    if run_name.startswith("imle_") or "rs_imle" in run_name:
        return "imle"
    if "joint_wam" in run_name:
        return "joint_latent_wam"
    return "flow_matching"


def dataset_label(config: dict[str, Any], run_name: str) -> str:
    value = nested(config, "deployment", "eval_bundle", "data_version")
    if value:
        return str(value)
    data_dir = nested(config, "data", "data_dir")
    if data_dir:
        return Path(str(data_dir)).name
    if "multitask600" in run_name or "multitask_box300_bottle300" in run_name:
        return "a2d_v3_multitask_box300_bottle300"
    return "未记录"


def build_record(run: Any, project_path: str) -> dict[str, Any]:
    config = dict(run.config or {})
    summary = dict(run.summary or {})
    name = str(run.name)
    policy = policy_name(config, summary, name)

    current_epoch = number(summary.get("epoch"))
    planned_epochs = number(nested(config, "training", "num_epochs"))
    current_step = number(first(summary, "global_step", "_step"))
    planned_steps = number(
        nested(config, "training", "max_train_steps")
        or config.get("max_train_steps")
    )
    if current_epoch is not None and planned_epochs:
        progress = min((float(current_epoch) + 1.0) / float(planned_epochs), 1.0)
    elif current_step is not None and planned_steps:
        progress = min(float(current_step) / float(planned_steps), 1.0)
    else:
        progress = 1.0 if str(run.state) == "finished" else None

    best_action = number(first(summary, "best_val_sample_action_mse", "best_action_mse.val_sample_action_mse"))
    current_action = number(first(summary, "val_sample_action_mse", "ema_val_sample_action_mse"))
    rdt_mse = number(first(summary, "overall_avg_sample_mse", "a2d_v3_multitask_sample_mse"))
    if best_action is not None:
        offline_metric = {"label": "best val action MSE", "value": best_action}
    elif rdt_mse is not None:
        offline_metric = {"label": "sample action MSE", "value": rdt_mse}
    elif current_action is not None:
        offline_metric = {"label": "current val action MSE", "value": current_action}
    else:
        offline_metric = None

    model = config.get("model") if isinstance(config.get("model"), dict) else {}
    training = config.get("training") if isinstance(config.get("training"), dict) else {}
    return {
        "wandb_run_id": str(run.id),
        "name": name,
        "state": str(run.state),
        "url": str(getattr(run, "url", f"https://wandb.ai/{project_path}/runs/{run.id}")),
        "created_at": str(getattr(run, "created_at", "")),
        "updated_at": str(getattr(run, "updated_at", "")),
        "group": str(getattr(run, "group", "") or ""),
        "job_type": str(getattr(run, "job_type", "") or ""),
        "tags": sorted(str(tag) for tag in (getattr(run, "tags", None) or [])),
        "policy_type": policy,
        "encoder": str(model.get("timm_model_name") or ("SigLIP SO400M" if policy == "rdt_170m_a2d" else "未记录")),
        "token_mode": str(model.get("timm_token_mode") or ("patch" if policy == "rdt_170m_a2d" else "未记录")),
        "tokens_per_frame": number(model.get("timm_tokens_per_frame")),
        "dataset": dataset_label(config, name),
        "batch_size": number(training.get("batch_size") or config.get("train_batch_size")),
        "current_epoch": current_epoch,
        "planned_epochs": planned_epochs,
        "current_step": current_step,
        "planned_steps": planned_steps,
        "progress": progress,
        "offline_metric": offline_metric,
        "best_epoch": number(summary.get("best_action_mse_epoch") or summary.get("best_epoch")),
        "latest_metrics": {
            "train_loss": number(first(summary, "train_loss", "loss")),
            "val_loss": number(summary.get("val_loss")),
            "val_action_mse": current_action,
            "val_lift_action_mse": number(summary.get("val_lift_sample_action_mse")),
        },
    }


def export_project(api: Any, project_path: str) -> dict[str, Any]:
    records = [build_record(run, project_path) for run in api.runs(project_path)]
    records.sort(key=lambda item: item["created_at"], reverse=True)
    return {
        "schema_version": 1,
        "generated_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "project": project_path,
        "project_url": f"https://wandb.ai/{project_path}",
        "runs": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default="z1135783608-psibot/a2d-flow-matching")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    import wandb

    payload = export_project(wandb.Api(timeout=30), args.project)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(args.output)
    print(json.dumps({"output": str(args.output), "runs": len(payload["runs"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
