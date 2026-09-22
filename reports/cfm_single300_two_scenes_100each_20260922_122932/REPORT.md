# cfm_single300_two_scenes_100each_20260922_122932

## 本轮目标与参数

| 项目 | 配置 |
|---|---|
| bottle · 目标 | 比较模型抓取表现，每模型 × 执行模式计划 100 次 |
| bottle · 模型 | cfm_bottle300_latest |
| bottle · 场景 | B19V2；headless |
| bottle · 执行 | 逐步 RPC＋GT（动作逐个下发）；H=16；每轮最多 300 个动作 |
| bottle · 种子 | 模型 seed=42；请求场景 seed 42…141（100 个，详见计划） |
| bottle · 成功判据 | 拇指＋至少另外两指接触力>1e-4 N，且抬升≥5 cm，连续5个动作后采样；之后掉落不扣分 |
| bottle · 初态 | 未启用布局恢复；相同 seed 不保证实际初态一致 |
| box · 目标 | 比较模型抓取表现，每模型 × 执行模式计划 100 次 |
| box · 模型 | cfm_box300_latest |
| box · 场景 | A10V1；headless |
| box · 执行 | 逐步 RPC＋GT（动作逐个下发）；H=16；每轮最多 300 个动作 |
| box · 种子 | 模型 seed=42；请求场景 seed 42…141（100 个，详见计划） |
| box · 成功判据 | 拇指＋至少另外两指接触力>1e-4 N，且抬升≥5 cm，连续5个动作后采样；之后掉落不扣分 |
| box · 初态 | 未启用布局恢复；相同 seed 不保证实际初态一致 |

参数来自各场景 `plan.json`；修改目标或参数时新建批次，历史报告保留原配置。

状态：**已完成**｜已记录 200/200 次｜更新：2026-09-22T22:00:05+08:00

| 场景 | 模型 | 已记录/计划 | 成功/有效 | 成功率 | 无效 | 失败现象：无接触/未达5cm/持续不足 |
|---|---|---:|---:|---:|---:|---|
| bottle | cfm_bottle300_latest | 100/100 | 45/97 | 46.4% | 3 | 37/11/4 |
| box | cfm_box300_latest | 100/100 | 56/98 | 57.1% | 2 | 22/15/5 |

成功按本批次原始记录口径；无效单列。失败分类是粗略观测现象，不代表已证实的因果。未结束回合不并入成功率。

原始批次：`/home/yurui/zhangyurui/test-result/cfm_single300_two_scenes_100each_20260922_122932`
配置与哈希：各场景 `plan.json`、`contract.json`；逐轮证据：`episodes.jsonl`、各回合 `samples.jsonl`。

- cfm_bottle300_latest：`/home/yurui/zhangyurui/ckpt/cfm_box300_bottle300_single_task_20260922/bottle300-latest-raw.tgz`；SHA256 `ab98fe312f1f8967e71fe45f7c1191adb5decb10e8cca49a2130d77b92dce874`

- cfm_box300_latest：`/home/yurui/zhangyurui/ckpt/cfm_box300_bottle300_single_task_20260922/box300-latest-raw.tgz`；SHA256 `afa7454cbc2e5b0867e60b3fe924b12df86e65b5c89f2d5e0f41593f5e82a16b`
