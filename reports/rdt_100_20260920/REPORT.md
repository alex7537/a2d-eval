# RDT latest · 两场景100次测试

## box · RDT 修复后50次测试

| 参数 | 设置 |
|---|---|
| 模型 | RDT170M latest raw step100000 |
| 场景/次数 | A10V1 / 50次 |
| 推理 | Step+GT+contact、H16、300动作、seed42 |
| 初始化 | 旧原生随机reset，场景seed42～91 |
| 判据 | 拇指+2指接触且抬升5cm，连续5采样 |

状态：completed

```json
{
  "attempts": 50,
  "completed": 49,
  "invalid": 1,
  "successes": 6,
  "success_rate": 0.12244897959183673
}
```

输入预处理parity未完全验证；本批为部署效果诊断。

证据：/home/yurui/zhangyurui/test-result/rdt_fixed_box_50_20260920_171335


## bottle · RDT 修复后50次测试

| 参数 | 设置 |
|---|---|
| 模型 | RDT170M latest raw step100000 |
| 场景/次数 | B19V2 / 50次 |
| 推理 | Step+GT+contact、H16、300动作、seed42 |
| 初始化 | 旧原生随机reset，场景seed42～91 |
| 判据 | 拇指+2指接触且抬升5cm，连续5采样 |

状态：completed

```json
{
  "attempts": 50,
  "completed": 47,
  "invalid": 3,
  "successes": 4,
  "success_rate": 0.0851063829787234
}
```

输入预处理parity未完全验证；本批为部署效果诊断。

证据：/home/yurui/zhangyurui/test-result/rdt_fixed_bottle_50_20260920_171335
