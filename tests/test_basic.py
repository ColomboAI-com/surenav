# tests/test_basic.py
import pytest
import asyncio
from surenav.proxy_manager import FreeProxyManager, Proxy
from surenav.fingerprint import FingerprintManager

def test_proxy_creation():
    proxy = Proxy(host="192.168.1.1", port=8080)
    assert proxy.url == "http://192.168.1.1:8080"
    assert proxy.protocol == "http"

def test_fingerprint_generation():
    fm = FingerprintManager()
    fp = fm.generate_fingerprint()
    assert "user_agent" in fp
    assert "viewport" in fp
    assert "width" in fp["viewport"]

@pytest.mark.asyncio
async def test_proxy_manager_fetch():
    pm = FreeProxyManager()
    # Just test that it initializes without error
    assert pm.proxies == []
    assert pm.working_proxies == []
