# cfm_bottle654_latest_100_20260922_213810

## 本轮目标与参数

| 项目 | 配置 |
|---|---|
| 目标 | 比较模型抓取表现，每模型 × 执行模式计划 100 次 |
| 模型 | cfm_bottle654_latest |
| 场景 | B19V2；headless |
| 执行 | 逐步 RPC＋GT（动作逐个下发）；H=16；每轮最多 300 个动作 |
| 种子 | 模型 seed=42；请求场景 seed 42…141（100 个，详见计划） |
| 成功判据 | 拇指＋至少另外两指接触力>1e-4 N，且抬升≥5 cm，连续5个动作后采样；之后掉落不扣分 |
| 初态 | 未启用布局恢复；相同 seed 不保证实际初态一致 |

参数来自各场景 `plan.json`；修改目标或参数时新建批次，历史报告保留原配置。

状态：**已完成**｜已记录 100/100 次｜更新：2026-09-23T14:58:50+08:00

| 场景 | 模型 | 已记录/计划 | 成功/有效 | 成功率 | 无效 | 失败现象：无接触/未达5cm/持续不足 |
|---|---|---:|---:|---:|---:|---|
| bottle | cfm_bottle654_latest | 100/100 | 54/95 | 56.8% | 5 | 20/14/7 |

成功按本批次原始记录口径；无效单列。失败分类是粗略观测现象，不代表已证实的因果。未结束回合不并入成功率。

原始批次：`/home/yurui/zhangyurui/test-result/cfm_bottle654_latest_100_20260922_213810`
配置与哈希：各场景 `plan.json`、`contract.json`；逐轮证据：`episodes.jsonl`、各回合 `samples.jsonl`。

- cfm_bottle654_latest：`/home/shared-assets/yurui-test-eval/ckpt-eval/9-4-cfm-new-task/b23v2_654ep_cfm_20260903_latest_best_raw/latest-raw.tgz`；SHA256 `0bf0d470cfaa6599f5f0374274690c57c29bb4d982db74581076837dc61ea4ee`
