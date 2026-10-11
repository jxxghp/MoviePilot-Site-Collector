# MoviePilot Site Collector

MoviePilot 站点适配采集器，独立维护源码、版本和跨平台下载。

[下载采集器](https://github.com/jxxghp/MoviePilot-Site-Collector/releases/latest) · [使用说明](docs/site-adapter-capture.md) · [发布说明](docs/site-adapter-collector-release.md)

采集器有变化时自动递增版本并发布 Windows、macOS 和 Linux 程序；文档、测试改动不发版。MoviePilot 主程序版本与本仓库完全分开。

## 开发与验证

使用 Python 3.14+，优先在仓库虚拟环境中运行：

```bash
python3.14 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m pytest -q
bash scripts/collect-site-adapter.sh
```

测试模拟网络和浏览器，不访问真实站点。打包、自动版本选择、测试构建以及历史版本迁移规则见 [发布说明](docs/site-adapter-collector-release.md#维护者发布流程)。

## 协作边界

本仓库生成脱敏采集 ZIP，MoviePilot-Build 消费采集包并生成站点适配。站点适配请求继续提交至 [MoviePilot 主仓](https://github.com/jxxghp/MoviePilot/issues/new?template=feature_request.yml)。协议 `format_version` 的变化需与消费方同步。

源码从 [MoviePilot](https://github.com/jxxghp/MoviePilot) 迁出，沿用 GPL-3.0 许可证。`1.0.1`～`1.0.3` 的源码快照保留原始提交出处，迁移附件保持原始文件内容和 SHA-256。
