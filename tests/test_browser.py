"""
Tests for StealthBrowser
"""
import pytest
from src.browser import StealthBrowser

def test_browser_init():
    """Test browser initialization"""
    browser = StealthBrowser()
    assert browser is not None
