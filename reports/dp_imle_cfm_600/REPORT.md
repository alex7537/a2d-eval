# dp_imle_cfm_latest_two_scenes_100each_20260917_214355

## 本轮目标与参数

| 项目 | 配置 |
|---|---|
| bottle · 目标 | 比较模型抓取表现，每模型 × 执行模式计划 100 次 |
| bottle · 模型 | dp_latest、imle_latest、cfm_latest |
| bottle · 场景 | B19V2；headless |
| bottle · 执行 | 逐步 RPC＋GT（动作逐个下发）；H=16；每轮最多 300 个动作 |
| bottle · 种子 | 模型 seed=42；请求场景 seed 42…141（100 个，详见计划） |
| bottle · 成功判据 | 拇指＋至少另外两指接触力>1e-4 N，且抬升≥5 cm，连续5个动作后采样；之后掉落不扣分 |
| bottle · 初态 | 未启用布局恢复；相同 seed 不保证实际初态一致 |
| box · 目标 | 比较模型抓取表现，每模型 × 执行模式计划 100 次 |
| box · 模型 | dp_latest、imle_latest、cfm_latest |
| box · 场景 | A10V1；headless |
| box · 执行 | 逐步 RPC＋GT（动作逐个下发）；H=16；每轮最多 300 个动作 |
| box · 种子 | 模型 seed=42；请求场景 seed 42…141（100 个，详见计划） |
| box · 成功判据 | 拇指＋至少另外两指接触力>1e-4 N，且抬升≥5 cm，连续5个动作后采样；之后掉落不扣分 |
| box · 初态 | 未启用布局恢复；相同 seed 不保证实际初态一致 |

参数来自各场景 `plan.json`；修改目标或参数时新建批次，历史报告保留原配置。

状态：**已完成**｜已记录 600/600 次｜更新：2026-09-18T22:18:40+08:00

| 场景 | 模型 | 已记录/计划 | 成功/有效 | 成功率 | 无效 | 失败现象：无接触/未达5cm/持续不足 |
|---|---|---:|---:|---:|---:|---|
| bottle | dp_latest | 100/100 | 68/94 | 72.3% | 6 | 17/3/6 |
| bottle | imle_latest | 100/100 | 60/98 | 61.2% | 2 | 17/16/5 |
| bottle | cfm_latest | 100/100 | 47/91 | 51.6% | 9 | 30/10/4 |
| box | dp_latest | 100/100 | 61/96 | 63.5% | 4 | 22/11/2 |
| box | imle_latest | 100/100 | 57/98 | 58.2% | 2 | 22/17/2 |
| box | cfm_latest | 100/100 | 52/93 | 55.9% | 7 | 29/9/3 |

成功按本批次原始记录口径；无效单列。失败分类是粗略观测现象，不代表已证实的因果。未结束回合不并入成功率。

原始批次：`/home/yurui/zhangyurui/test-result/dp_imle_cfm_latest_two_scenes_100each_20260917_214355`
配置与哈希：各场景 `plan.json`、`contract.json`；逐轮证据：`episodes.jsonl`、各回合 `samples.jsonl`。

- dp_latest：`/home/yurui/zhangyurui/ckpt/dp_multitask_100ep_best_raw_latest_20260911/dp-multitask-latest-raw.tgz`；SHA256 `f1e537b09f9be8e5b83a387ff51f19345f47dc79087133328cfc0836c4771645`
- imle_latest：`/home/yurui/zhangyurui/ckpt/imle_multitask_box300_bottle300_100ep_best_ema_latest_20260908/imle-multitask-latest-raw.tgz`；SHA256 `13d6db49752a89dfdab93ee77481835300ac412b2b37fd142b27951d028ad3b7`
- cfm_latest：`/home/shared-assets/yurui-test-eval/ckpt-eval/9-4-muti-cfm/multitask_box300_bottle300_cfm_20260904_latest_best_raw/latest-raw.tgz`；SHA256 `fb3fb5ce87d7e9294aead49f03054362bb557ee9c2f97986645a0b46691a4117`

- dp_latest：`/home/yurui/zhangyurui/ckpt/dp_multitask_100ep_best_raw_latest_20260911/dp-multitask-latest-raw.tgz`；SHA256 `f1e537b09f9be8e5b83a387ff51f19345f47dc79087133328cfc0836c4771645`
- imle_latest：`/home/yurui/zhangyurui/ckpt/imle_multitask_box300_bottle300_100ep_best_ema_latest_20260908/imle-multitask-latest-raw.tgz`；SHA256 `13d6db49752a89dfdab93ee77481835300ac412b2b37fd142b27951d028ad3b7`
- cfm_latest：`/home/shared-assets/yurui-test-eval/ckpt-eval/9-4-muti-cfm/multitask_box300_bottle300_cfm_20260904_latest_best_raw/latest-raw.tgz`；SHA256 `fb3fb5ce87d7e9294aead49f03054362bb557ee9c2f97986645a0b46691a4117`
