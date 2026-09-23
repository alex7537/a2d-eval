# dp_multitask_bottle_denoise8_20260923_194750

## 本轮目标与参数

| 项目 | 配置 |
|---|---|
| 目标 | 比较模型抓取表现，每模型 × 执行模式计划 30 次 |
| 模型 | dp_latest |
| 场景 | B19V2；headless |
| 执行 | 逐步 RPC＋GT（动作逐个下发）；H=16；每轮最多 300 个动作 |
| 种子 | 模型 seed=42；请求场景 seed 42…71（30 个，详见计划） |
| 成功判据 | 拇指＋至少另外两指接触力>1e-4 N，且抬升≥5 cm，连续5个动作后采样；之后掉落不扣分 |
| 初态 | 未启用布局恢复；相同 seed 不保证实际初态一致 |

参数来自各场景 `plan.json`；修改目标或参数时新建批次，历史报告保留原配置。

状态：**已完成**｜已记录 30/30 次｜更新：2026-09-24T01:49:45+08:00

| 场景 | 模型 | 已记录/计划 | 成功/有效 | 成功率 | 无效 | 失败现象：无接触/未达5cm/持续不足 |
|---|---|---:|---:|---:|---:|---|
| bottle | dp_latest | 30/30 | 17/28 | 60.7% | 2 | 6/4/1 |

成功按本批次原始记录口径；无效单列。失败分类是粗略观测现象，不代表已证实的因果。未结束回合不并入成功率。

原始批次：`/home/yurui/zhangyurui/test-result/dp_multitask_bottle_denoise8_20260923_194750`
配置与哈希：各场景 `plan.json`、`contract.json`；逐轮证据：`episodes.jsonl`、各回合 `samples.jsonl`。

- dp_latest：`/home/yurui/zhangyurui/ckpt/dp_multitask_100ep_best_raw_latest_20260911/dp-multitask-latest-raw.tgz`；SHA256 `f1e537b09f9be8e5b83a387ff51f19345f47dc79087133328cfc0836c4771645`
