# eval_v2_partial_archive_20260929_163422

## 本轮目标与参数

| 项目 | 配置 |
|---|---|
| bottle · 目标 | 比较模型抓取表现，每模型 × 执行模式计划 268 次 |
| bottle · 模型 | dp_latest、imle_latest、cfm_latest |
| bottle · 场景 | bottle；headless |
| bottle · 执行 | 逐步 RPC＋GT（动作逐个下发）；H=16；每轮最多 300 个动作 |
| bottle · 种子 | 模型 seed=42；请求场景 seed 42…109（268 个，详见计划） |
| bottle · 成功判据 | 拇指＋至少另外两指接触力>1e-4 N，且抬升≥5 cm，连续5个动作后采样；之后掉落不扣分 |
| bottle · 初态 | 布局恢复已启用（是否配对须看验收） |
| box · 目标 | 比较模型抓取表现，每模型 × 执行模式计划 239 次 |
| box · 模型 | dp_latest、imle_latest、cfm_latest |
| box · 场景 | box；headless |
| box · 执行 | 逐步 RPC＋GT（动作逐个下发）；H=16；每轮最多 300 个动作 |
| box · 种子 | 模型 seed=42；请求场景 seed 42…80（239 个，详见计划） |
| box · 成功判据 | 拇指＋至少另外两指接触力>1e-4 N，且抬升≥5 cm，连续5个动作后采样；之后掉落不扣分 |
| box · 初态 | 布局恢复已启用（是否配对须看验收） |

参数来自各场景 `plan.json`；修改目标或参数时新建批次，历史报告保留原配置。

状态：**异常停止／未完成**｜已记录 1515/1521 次｜更新：2026-09-29T16:34:22+08:00

| 场景 | 模型 | 已记录/计划 | 成功/有效 | 成功率 | 无效 | 失败现象：无接触/未达5cm/持续不足 |
|---|---|---:|---:|---:|---:|---|
| bottle | dp_latest | 267/268 | 34/51 | 66.7% | 216 | 8/6/3 |
| bottle | imle_latest | 267/268 | 39/51 | 76.5% | 216 | 3/4/5 |
| bottle | cfm_latest | 267/268 | 30/51 | 58.8% | 216 | 13/7/1 |
| box | dp_latest | 238/239 | 10/18 | 55.6% | 220 | 7/1/0 |
| box | imle_latest | 238/239 | 12/18 | 66.7% | 220 | 2/4/0 |
| box | cfm_latest | 238/239 | 12/17 | 70.6% | 221 | 4/1/0 |

成功按本批次原始记录口径；无效单列。失败分类是粗略观测现象，不代表已证实的因果。未结束回合不并入成功率。

原始批次：`/home/yurui/zhangyurui/test-result/eval_v2_partial_archive_20260929_163422`
配置与哈希：各场景 `plan.json`、`contract.json`；逐轮证据：`episodes.jsonl`、各回合 `samples.jsonl`。

- dp_latest：`/home/yurui/zhangyurui/ckpt/dp_multitask_100ep_best_raw_latest_20260911/dp-multitask-latest-raw.tgz`；SHA256 `f1e537b09f9be8e5b83a387ff51f19345f47dc79087133328cfc0836c4771645`
- imle_latest：`/home/yurui/zhangyurui/ckpt/imle_multitask_box300_bottle300_100ep_best_ema_latest_20260908/imle-multitask-latest-raw.tgz`；SHA256 `13d6db49752a89dfdab93ee77481835300ac412b2b37fd142b27951d028ad3b7`
- cfm_latest：`/home/shared-assets/yurui-test-eval/ckpt-eval/9-4-muti-cfm/multitask_box300_bottle300_cfm_20260904_latest_best_raw/latest-raw.tgz`；SHA256 `fb3fb5ce87d7e9294aead49f03054362bb557ee9c2f97986645a0b46691a4117`

- dp_latest：`/home/yurui/zhangyurui/ckpt/dp_multitask_100ep_best_raw_latest_20260911/dp-multitask-latest-raw.tgz`；SHA256 `f1e537b09f9be8e5b83a387ff51f19345f47dc79087133328cfc0836c4771645`
- imle_latest：`/home/yurui/zhangyurui/ckpt/imle_multitask_box300_bottle300_100ep_best_ema_latest_20260908/imle-multitask-latest-raw.tgz`；SHA256 `13d6db49752a89dfdab93ee77481835300ac412b2b37fd142b27951d028ad3b7`
- cfm_latest：`/home/shared-assets/yurui-test-eval/ckpt-eval/9-4-muti-cfm/multitask_box300_bottle300_cfm_20260904_latest_best_raw/latest-raw.tgz`；SHA256 `fb3fb5ce87d7e9294aead49f03054362bb557ee9c2f97986645a0b46691a4117`

## 本次归档说明

这是2026-09-29冻结的未完成快照，不代表600有效回合目标达成。共有206个有效回合。其余1309条为无效/中断占位记录，其中包含模型尚未执行就因其他模型或启动失败而补写的记录，不能理解为1309次实际抓取，也不纳入成功率。原始记录保留，不删除。

协议：eval2固定初态恢复，H16/300动作/模型seed42，每动作4个120Hz物理步（同步30Hz）；查询/推理期间不推进。Box与Bottle分别统计。100布局含无效低位初态，补测循环使用布局，因此有效回合数不等于不同布局数。失败原因：显存不足导致加载失败，另有reset时服务连接关闭尚未解决。当前原监督器保持不动，本文件只归档截至时间的结果。
