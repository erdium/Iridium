"""
Iridium - A simple, elegant, and powerful wrapper around Selenium WebDriver.
"""

from .browser import Browser
from .element import Element
from .wait import until

__version__ = "2.0.1"
__author__ = "Iridium Contributors"
__license__ = "MIT"

__all__ = ["Browser", "Element", "until"]
