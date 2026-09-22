# single_box_dp_imle_cfm_100each_20260921_114739

## 本轮目标与参数

| 项目 | 配置 |
|---|---|
| 目标 | 比较模型抓取表现，每模型 × 执行模式计划 100 次 |
| 模型 | dp_latest、imle_latest、cfm_latest |
| 场景 | A10V1；headless |
| 执行 | 逐步 RPC＋GT（动作逐个下发）；H=16；每轮最多 300 个动作 |
| 种子 | 模型 seed=42；请求场景 seed 42…141（100 个，详见计划） |
| 成功判据 | 拇指＋至少另外两指接触力>1e-4 N，且抬升≥5 cm，连续5个动作后采样；之后掉落不扣分 |
| 初态 | 未启用布局恢复；相同 seed 不保证实际初态一致 |

参数来自各场景 `plan.json`；修改目标或参数时新建批次，历史报告保留原配置。

状态：**已完成**｜已记录 300/300 次｜更新：2026-09-21T21:12:12+08:00

| 场景 | 模型 | 已记录/计划 | 成功/有效 | 成功率 | 无效 | 失败现象：无接触/未达5cm/持续不足 |
|---|---|---:|---:|---:|---:|---|
| box | dp_latest | 100/100 | 67/96 | 69.8% | 4 | 18/10/1 |
| box | imle_latest | 100/100 | 66/98 | 67.3% | 2 | 24/8/0 |
| box | cfm_latest | 100/100 | 56/93 | 60.2% | 7 | 21/14/2 |

成功按本批次原始记录口径；无效单列。失败分类是粗略观测现象，不代表已证实的因果。未结束回合不并入成功率。

原始批次：`/home/yurui/zhangyurui/test-result/single_box_dp_imle_cfm_100each_20260921_114739`
配置与哈希：各场景 `plan.json`、`contract.json`；逐轮证据：`episodes.jsonl`、各回合 `samples.jsonl`。

- dp_latest：`/home/shared-assets/yurui-test-eval/ckpt-eval/8-31-flow-post_dp_imle/dp-latest-raw-raw.tgz`；SHA256 `4976c2b781e575d2e470d60d1ad197a9dc6d6edd7e70f1507b5882cc0170facd`
- imle_latest：`/home/shared-assets/yurui-test-eval/ckpt-eval/8-31-flow-post_dp_imle/imle-latest-raw-raw.tgz`；SHA256 `534c95854662cdaffe3178faf75bac0f13677d32842f88624617fac50122f32b`
- cfm_latest：`/home/shared-assets/yurui-test-eval/ckpt-eval/8-31-flow-post_dp_imle/cfm-post-latest-raw-raw.tgz`；SHA256 `7cb75edd11acdedf04c9181be7ddc836c67bd4d3024268e899cbab489fb8b14a`
