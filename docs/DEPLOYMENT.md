# SureNav Deployment Guide

## Docker Deployment

### Build Image
```bash
docker build -t surenav:latest .
```

### Run Container
```bash
docker run -d -p 8000:8000 surenav:latest
```

## Local Deployment

### Install Dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### Run Server
```bash
python -m uvicorn src.server:app --host 0.0.0.0 --port 8000
```

## Environment Variables
- `SURENAV_PORT`: Server port (default: 8000)
- `SURENAV_PROXY_REFRESH`: Proxy refresh interval in seconds (default: 300)
- `SURENAV_HEADLESS`: Run browser headless (default: true)
- `SURENAV_MAX_RETRIES`: Max retry attempts (default: 3)
