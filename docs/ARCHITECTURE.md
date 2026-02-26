# SureNav Architecture

## Overview
SureNav is built with a modular architecture for web scraping and browser automation.

## Components

### 1. StealthBrowser
- Playwright-based browser automation
- Anti-detection fingerprinting
- JavaScript rendering

### 2. FreeProxyManager
- Aggregates free proxies from multiple sources
- Validates and rotates proxies
- Handles proxy failures

### 3. GoogleSearcher
- Scrapes Google search results
- Bypasses rate limiting
- Returns structured data

### 4. FastAPI Server
- RESTful API endpoints
- Async request handling
- Health monitoring

## Data Flow
```
Client → FastAPI → ProxyManager → StealthBrowser → Target Site → Response
```
