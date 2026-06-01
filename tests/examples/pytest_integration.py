"""
Pytest Integration Example

Demonstrates:
- Writing browser tests with pytest
- Using fixtures for browser management
- Parametrized tests

Usage:
    pytest pytest_integration.py -v
"""

import pytest
from iridium import Browser


@pytest.fixture(scope="module")
def browser():
    """Create a browser instance for the test module."""
    b = Browser()
    b.get("https://www.python.org")
    yield b
    b.quit()


def test_page_title(browser):
    """Test that the page title contains 'Python'."""
    assert "Python" in browser.title


def test_search_box_present(browser):
    """Test that search box is present on the page."""
    search_input = browser.find_element_by_name("q")
    assert search_input.is_displayed()


def test_navigation_count(browser):
    """Test that there are navigation links on the page."""
    nav_links = browser.find_elements_by_css("nav a")
    assert len(nav_links) > 0


@pytest.mark.parametrize("link_text", ["Downloads", "Documentation", "Community"])
def test_nav_link_visible(browser, link_text):
    """Test that specific navigation links are visible."""
    link = browser.find_element_by_partial_text(link_text)
    assert link.is_displayed()
