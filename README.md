# A2D Eval

独立维护 A2D 模型评测协议、结果审计及自动报告。当前首版迁入已有测评分支的诊断和报告工具；真实 Isaac 执行仍由现有冻结 runner 完成，尚未迁入通用运行后端。

## 当前能力

| 模块 | 状态 |
|---|---|
| bundle接收、哈希校验、测试合约冻结 | 已迁入 |
| 结果汇总、覆盖检查、失败分类、统计区间 | 已迁入 |
| 完成/中断报告、Obsidian输出 | 已迁入 |
| DP/IMLE/CFM/WAM/RDT统一执行后端 | 待迁移，不影响正在运行的测试 |
| 固定布局保存恢复 | 实验阶段，未纳入稳定入口 |

工作流：训练导出bundle → 外部仿真runner测试 → 本仓库审计与报告 → 人工决定下一轮训练。

```bash
PYTHONPATH=tools/a2d_eval_loop python3 -m unittest discover -s tools/a2d_eval_loop/tests -v
python3 tools/a2d_eval_loop/loop.py --help
python3 tools/a2d_eval_loop/watch_eval_to_obsidian.py --help
```

[使用说明](tools/a2d_eval_loop/README.md)。依赖及命令以该工具说明为准。

## 边界

训练仓库维护模型与bundle导出；仿真仓库维护资产、机器人、传感器和gRPC；本仓库维护评测与报告。skill定义操作规则，Obsidian保存结论。

权重、资产、原始日志及视频放在仓库外；测试记录引用路径与哈希。历史随机初态、异步step+GT与实验恢复协议分开统计，禁止混合排名。

首版不启动训练或仿真，不自动发布结果。当前RDT任务继续使用原冻结脚本。

## 迁入来源

来自 `alex7537/flow-matching-test-a2d-v2` 的测评工作树，具体源commit及文件哈希见 [PROVENANCE.json](PROVENANCE.json)。包含本地已验证的暂停快照排除修复；未导入运行结果和机器凭证。
