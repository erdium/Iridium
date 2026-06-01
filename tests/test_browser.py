"""
Tests for the Browser class.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from selenium.common.exceptions import NoSuchElementException

from iridium import Browser


class TestBrowserInitialization:
    """Tests for Browser initialization."""

    @patch("iridium.browser.webdriver.Chrome")
    def test_default_initialization(self, mock_chrome):
        """Test that Browser initializes with default values."""
        mock_chrome.return_value = MagicMock()
        browser = Browser()
        assert browser is not None
        browser.quit()

    @patch("iridium.browser.webdriver.Firefox")
    def test_firefox_initialization(self, mock_firefox):
        """Test Browser initialization with Firefox."""
        mock_firefox.return_value = MagicMock()
        browser = Browser(browser="firefox")
        assert browser is not None
        browser.quit()

    def test_unsupported_browser(self):
        """Test that unsupported browser raises ValueError."""
        with pytest.raises(ValueError, match="Unsupported browser"):
            Browser(browser="invalid_browser")


class TestBrowserContextManager:
    """Tests for context manager functionality."""

    @patch("iridium.browser.webdriver.Chrome")
    def test_context_manager_quits_browser(self, mock_chrome):
        """Test that browser quits on context manager exit."""
        mock_instance = MagicMock()
        mock_chrome.return_value = mock_instance

        with Browser() as browser:
            assert browser is not None

        mock_instance.quit.assert_called_once()


class TestElementFinding:
    """Tests for element finding methods."""

    @patch("iridium.browser.webdriver.Chrome")
    def test_find_element_by_id(self, mock_chrome):
        """Test finding element by ID."""
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver

        browser = Browser()
        browser.find_element_by_id("test-id")

        mock_driver.find_element.assert_called_once()
        browser.quit()

    @patch("iridium.browser.webdriver.Chrome")
    def test_find_element_by_css(self, mock_chrome):
        """Test finding element by CSS selector."""
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver

        browser = Browser()
        browser.find_element_by_css(".my-class")

        mock_driver.find_element.assert_called_once()
        browser.quit()

    @patch("iridium.browser.webdriver.Chrome")
    def test_find_element_by_text(self, mock_chrome):
        """Test finding element by exact text."""
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver

        browser = Browser()
        browser.find_element_by_text("Hello World")

        mock_driver.find_element.assert_called_once()
        browser.quit()


class TestWindowManagement:
    """Tests for window and tab management."""

    @patch("iridium.browser.webdriver.Chrome")
    def test_maximize_window(self, mock_chrome):
        """Test window maximization."""
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver

        browser = Browser()
        browser.maximize_window()

        mock_driver.maximize_window.assert_called_once()
        browser.quit()


class TestCookieManagement:
    """Tests for cookie operations."""

    @patch("iridium.browser.webdriver.Chrome")
    def test_add_cookie(self, mock_chrome):
        """Test adding a cookie."""
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver

        browser = Browser()
        browser.add_cookie({"name": "session", "value": "abc123"})

        mock_driver.add_cookie.assert_called_once_with(
            {"name": "session", "value": "abc123"}
        )
        browser.quit()

    @patch("iridium.browser.webdriver.Chrome")
    def test_delete_all_cookies(self, mock_chrome):
        """Test deleting all cookies."""
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver

        browser = Browser()
        browser.delete_all_cookies()

        mock_driver.delete_all_cookies.assert_called_once()
        browser.quit()
