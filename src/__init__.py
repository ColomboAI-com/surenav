"""
SureNav - Open-source web unblocker for AI agents
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .browser import StealthBrowser
from .proxy_manager import FreeProxyManager
from .search import GoogleSearcher

__all__ = ["StealthBrowser", "FreeProxyManager", "GoogleSearcher"]
