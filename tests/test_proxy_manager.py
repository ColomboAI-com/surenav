"""
Tests for FreeProxyManager
"""
import pytest
from src.proxy_manager import FreeProxyManager

def test_proxy_manager_init():
    """Test proxy manager initialization"""
    manager = FreeProxyManager()
    assert manager is not None
