#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
port="${PORT:-8080}"
command -v python3 >/dev/null || { echo '请先安装 Python 3。'; exit 1; }
echo '正在获取最新看板和测试结果……'
git pull --ff-only
[[ -f reports/latest/results.json ]] || { echo '未找到测试结果，请联系仓库维护者。'; exit 1; }
printf '\n看板即将启动。\n本机浏览器打开：http://localhost:%s\n远程部署打开：http://服务器IP:%s（需要网络允许访问）\n按 Ctrl+C 停止服务。\n\n' "$port" "$port"
exec python3 -m http.server "$port" --bind 0.0.0.0 --directory reports/latest
