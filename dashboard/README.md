# 测评结果静态归档

看板还可以合并一份隐私裁剪后的W&B训练快照：

```bash
python3 dashboard/sync_wandb_runs.py \
  --project z1135783608-psibot/a2d-flow-matching \
  --output dashboard/training_runs.json
```

该命令只读W&B，并且只输出白名单配置和summary字段；不输出API key、
`.netrc`、完整数据路径或checkpoint路径。执行环境必须自行具备W&B读权限。
`dashboard/model_registry.json`显式记录`run ID → checkpoint role/step → bundle
SHA/测评批次`，禁止通过相似名称自动猜测模型关系。

完成／暂停／中断时，仓库 observer 默认生成 `<batch>/static_report/`，与本地和 Ob 报告使用同一份汇总计数。现有旧 observer 进程不会自动加载新代码；新任务使用本仓库入口，历史批次可手动导出。

```bash
python3 dashboard/export_report.py --batch /path/to/batch --output /path/to/site
python3 -m http.server 8080 --bind 0.0.0.0 --directory /path/to/site
```

同事复制整个 site 文件夹即可部署，也可以由 Nginx 等静态服务器托管在子路径。无需仿真环境或原始测试目录。访问服务器 IP:8080；网络需允许该端口。

包含 index.html、evaluation.html、app.js、style.css、results.json、REPORT.md。
`index.html`为训练模型页，`evaluation.html`为完整测评页；`results.json`同时
包含训练快照和测评结果。结果不实时更新；重新同步W&B、导出并提交后才更新。
REPORT.md 保留原始证据路径，分享前核对接收范围。

上传独立于导出：将 static_report 内容复制至约定结果仓库目录后提交、推送；上传失败不影响本地/Ob归档。自动推送由下文 --publish-remote 显式启用。不要把模型、原始日志、视频或凭证放入静态目录。

适用输入是本仓库 observer 的 auto_report_status.json＋AUTO_REPORT.md＋场景 plan.json。独立 RDT runner 等不同 schema 必须先适配报告，不能伪称全部 runner 已自动接入。

## 终态自动上传

为已授权批次启动 observer 时增加：
```bash
python3 tools/a2d_eval_loop/watch_eval_to_obsidian.py --batch /path/to/batch --vault /path/to/vault --publish-remote git@github.com:alex7537/a2d-eval.git --publish-branch main
```
完成／暂停／中断后导出并发布到 reports/<批次名>，同时更新 reports/latest。临时克隆合并，保留其他结果及训练数据；不修改运行 checkout。需要本机已具备 GitHub SSH 写权限。最多重试3次，结果写 publish_status.json；失败不会撤回本地/Ob报告。旧进程不会自动升级。

补传已导出的批次：
```bash
python3 dashboard/publish_report.py --batch /path/to/batch --remote git@github.com:alex7537/a2d-eval.git
```
