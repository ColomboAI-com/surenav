"""
SureNav FastAPI Server
"""
import logging
import os
from typing import Optional
from fastapi import FastAPI, HTTPException, Query, Header
from fastapi.responses import HTMLResponse, JSONResponse
import asyncio

from .browser import StealthBrowser
from .proxy_manager import FreeProxyManager
from .search import GoogleSearcher

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="SureNav", 
    description="Open-source web unblocker - no API keys required", 
    version="1.0.0"
)

proxy_manager = FreeProxyManager()
browser: Optional[StealthBrowser] = None
searcher: Optional[GoogleSearcher] = None

@app.on_event("startup")
async def startup():
    global browser, searcher
    asyncio.create_task(proxy_manager.refresh_proxies())
    await proxy_manager.fetch_proxies()
    await proxy_manager.validate_proxies(max_proxies=20)
    browser = StealthBrowser(proxy_manager)
    await browser.start()
    searcher = GoogleSearcher(browser)
    logger.info("SureNav started successfully")

@app.on_event("shutdown")
async def shutdown():
    if browser:
        await browser.stop()

@app.get("/")
async def root():
    return {
        "name": "SureNav", 
        "description": "Open-source web unblocker by ColomboAI", 
        "endpoints": {
            "/browser": "Fetch web pages",
            "/search": "Google search",
            "/health": "Health check"
        }
    }

@app.get("/browser", response_class=HTMLResponse)
async def browser_get(
    url: str = Query(..., description="Target URL to fetch"),
    format: str = Query("rendered", description="rendered or raw"),
    delay: float = Query(0, description="Extra delay for dynamic content"),
    device: str = Query("desktop", description="desktop or mobile"),
    authorization: Optional[str] = Header(None)
):
    if not browser:
        raise HTTPException(status_code=503, detail="Browser not initialized")
    
    result = await browser.fetch_page(
        url=url, 
        format=format, 
        delay=delay, 
        device_type=device
    )
    
    if not result['success']:
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to fetch page: {result.get('error')}"
        )
    
    return HTMLResponse(content=result['content'])

@app.get("/search")
async def search_get(
    terms: str = Query(..., description="Search query"),
    format: str = Query("html", description="html or json"),
    serps: int = Query(1, description="Number of result pages"),
    size: Optional[int] = Query(None, description="Results per page (max 100)"),
    offset: int = Query(0, description="Skip first N results"),
    language: Optional[str] = Query(None, description="Language code"),
    authorization: Optional[str] = Header(None)
):
    if not searcher:
        raise HTTPException(status_code=503, detail="Search not initialized")
    
    result = await searcher.search(
        terms=terms, 
        format=format, 
        serps=serps, 
        size=size, 
        offset=offset, 
        language=language
    )
    
    if not result['success']:
        raise HTTPException(
            status_code=500, 
            detail=f"Search failed: {result.get('error')}"
        )
    
    if format == "json":
        return JSONResponse(content=result)
    else:
        return HTMLResponse(content=result['content'])

@app.get("/health")
async def health():
    return {
        "status": "healthy", 
        "proxies_available": len(proxy_manager.working_proxies), 
        "browser_ready": browser is not None,
        "version": "1.0.0"
    }

def main():
    """Entry point for console script."""
    import uvicorn
    port = int(os.getenv("SURENAV_PORT", 8000))
    uvicorn.run(
        "surenav.server:app", 
        host="0.0.0.0", 
        port=port, 
        reload=False
    )

if __name__ == "__main__":
    main()
