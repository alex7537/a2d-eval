# 测评结果静态归档

完成／暂停／中断时，仓库 observer 默认生成 `<batch>/static_report/`，与本地和 Ob 报告使用同一份汇总计数。现有旧 observer 进程不会自动加载新代码；新任务使用本仓库入口，历史批次可手动导出。

```bash
python3 dashboard/export_report.py --batch /path/to/batch --output /path/to/site
python3 -m http.server 8080 --bind 0.0.0.0 --directory /path/to/site
```

同事复制整个 site 文件夹即可部署，也可以由 Nginx 等静态服务器托管在子路径。无需仿真环境或原始测试目录。访问服务器 IP:8080；网络需允许该端口。

包含 index.html、app.js、style.css、results.json、REPORT.md。结果不实时更新；重新导出并同步文件后更新。REPORT.md 保留原始证据路径，分享前核对接收范围。

上传独立于导出：将 static_report 内容复制至约定结果仓库目录后提交、推送；上传失败不影响本地/Ob归档。当前未配置自动推送目的地，不会自动执行 git push。不要把模型、原始日志、视频或凭证放入静态目录。

适用输入是本仓库 observer 的 auto_report_status.json＋AUTO_REPORT.md＋场景 plan.json。独立 RDT runner 等不同 schema 必须先适配报告，不能伪称全部 runner 已自动接入。
