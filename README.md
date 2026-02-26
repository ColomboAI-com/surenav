# 🧭 SureNav

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

**SureNav** is a fully open-source web navigation and scraping toolkit for AI agents that requires **zero API keys**. It provides anti-detection browser automation, intelligent proxy rotation, and web unblocking capabilities—completely free.

## ✨ Features

- 🔓 **No API Keys Required** - Uses free proxy aggregation and local browser automation
- 🕵️ **Stealth Mode** - Advanced anti-detection with fingerprint randomization
- 🌍 **Global Proxy Network** - Auto-rotating free proxies from multiple sources
- ⚡ **JavaScript Rendering** - Full browser automation for modern web apps
- 🔍 **Google Search** - Scrape search results without rate limits
- 🐳 **Docker Ready** - One-command deployment
- 🔌 **API Compatible** - Similar interface to popular paid services

## 🚀 Quick Start

### Docker (Easiest)

```bash
docker run -p 8000:8000 ghcr.io/colomboai-com/surenav:latest
```

### Local Installation

```bash
pip install surenav
playwright install chromium
surenav-server
```

## 📖 Usage

### Fetch a Web Page

```bash
curl "http://localhost:8000/browser?url=https://example.com"
```

### Search Google

```bash
# JSON output
curl "http://localhost:8000/search?terms=open+source+ai&format=json"

# HTML output
curl "http://localhost:8000/search?terms=python+tutorial"
```

### Python SDK

```python
from surenav import StealthBrowser

browser = StealthBrowser()
result = await browser.fetch_page("https://example.com")
print(result["content"])
```

## 🏗️ Architecture

```mermaid
graph TD
    A[Client Request] --> B[FastAPI Server]
    B --> C[Proxy Manager]
    C --> D[Free Proxy Lists]
    B --> E[Stealth Browser]
    E --> F[Playwright + Stealth]
    F --> G[Target Website]
    G --> H[Clean Content]
```

## ⚙️ Configuration

Environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `SURENAV_PORT` | 8000 | Server port |
| `SURENAV_PROXY_REFRESH` | 300 | Proxy refresh interval (seconds) |
| `SURENAV_HEADLESS` | true | Run browser headless |
| `SURENAV_MAX_RETRIES` | 3 | Retry attempts per request |

## 🛡️ Anti-Detection Features

- ✅ User agent rotation
- ✅ Viewport fingerprint randomization
- ✅ WebGL/Canvas noise injection
- ✅ Automation flag removal
- ✅ Mouse movement humanization
- ✅ Cookie/session handling
- ✅ TLS/JA3 fingerprint randomization (planned)

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📜 License

MIT - Free for personal and commercial use.
