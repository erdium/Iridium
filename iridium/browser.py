"""
Browser module - Main entry point for browser automation.
"""

import time
import logging
from typing import Optional, List, Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from .element import Element

logger = logging.getLogger(__name__)


class Browser:
    """
    A high-level wrapper around Selenium WebDriver.

    Provides simplified methods for browser automation, including
    smart element location, automatic waits, and human-friendly API.
    """

    SUPPORTED_BROWSERS = ["chrome", "firefox", "safari", "edge", "opera"]

    def __init__(
        self,
        browser: str = "chrome",
        options: Optional[webdriver.ChromeOptions] = None,
        implicit_wait: int = 10,
        driver_path: Optional[str] = None,
        use_webdriver_manager: bool = True,
    ):
        """
        Initialize a Browser instance.

        Args:
            browser: Browser name. One of "chrome", "firefox", "safari", "edge", "opera".
            options: Selenium options object for the chosen browser.
            implicit_wait: Implicit wait time in seconds.
            driver_path: Path to WebDriver executable. If None and
                         use_webdriver_manager is True, driver is auto-managed.
            use_webdriver_manager: Automatically download and manage WebDriver binary.

        Raises:
            ValueError: If an unsupported browser name is provided.
        """
        if browser.lower() not in self.SUPPORTED_BROWSERS:
            raise ValueError(
                f"Unsupported browser '{browser}'. "
                f"Supported browsers: {', '.join(self.SUPPORTED_BROWSERS)}"
            )

        self._browser_name = browser.lower()
        self._implicit_wait = implicit_wait
        self._driver = None

        if options is None:
            options = self._default_options()

        self._driver = self._create_driver(
            options=options,
            driver_path=driver_path,
            use_webdriver_manager=use_webdriver_manager,
        )

        self._driver.implicitly_wait(implicit_wait)
        self._wait = WebDriverWait(self._driver, implicit_wait)

        logger.info(f"Browser '{self._browser_name}' initialized successfully.")

    def _default_options(self):
        """Return default options for the selected browser."""
        if self._browser_name == "chrome":
            return webdriver.ChromeOptions()
        elif self._browser_name == "firefox":
            return webdriver.FirefoxOptions()
        elif self._browser_name == "edge":
            return webdriver.EdgeOptions()
        elif self._browser_name == "safari":
            return webdriver.SafariOptions()
        elif self._browser_name == "opera":
            return webdriver.ChromeOptions()  # Opera uses Chromium options
        return webdriver.ChromeOptions()

    def _create_driver(
        self,
        options,
        driver_path: Optional[str] = None,
        use_webdriver_manager: bool = True,
    ) -> WebDriver:
        """Create and return a WebDriver instance."""
        if self._browser_name == "chrome":
            if driver_path:
                service = ChromeService(executable_path=driver_path)
            elif use_webdriver_manager:
                service = ChromeService(ChromeDriverManager().install())
            else:
                service = None
            return webdriver.Chrome(service=service, options=options)

        elif self._browser_name == "firefox":
            if driver_path:
                service = FirefoxService(executable_path=driver_path)
            elif use_webdriver_manager:
                service = FirefoxService(GeckoDriverManager().install())
            else:
                service = None
            return webdriver.Firefox(service=service, options=options)

        elif self._browser_name == "safari":
            return webdriver.Safari(options=options)

        elif self._browser_name == "edge":
            return webdriver.Edge(options=options)

        elif self._browser_name == "opera":
            return webdriver.Chrome(options=options)

        raise ValueError(f"Cannot create driver for '{self._browser_name}'.")

    def __enter__(self):
        """Enable context manager usage."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close browser on context manager exit."""
        self.quit()

    def get(self, url: str) -> None:
        """
        Navigate to a URL.

        Args:
            url: The URL to navigate to.
        """
        logger.info(f"Navigating to {url}")
        self._driver.get(url)

    def quit(self) -> None:
        """Close the browser and end the session."""
        if self._driver:
            logger.info("Closing browser.")
            self._driver.quit()
            self._driver = None

    @property
    def title(self) -> str:
        """Return the current page title."""
        return self._driver.title

    @property
    def current_url(self) -> str:
        """Return the current page URL."""
        return self._driver.current_url

    @property
    def page_source(self) -> str:
        """Return the current page source."""
        return self._driver.page_source

    @property
    def window_handles(self) -> List[str]:
        """Return handles of all open browser windows/tabs."""
        return self._driver.window_handles

    @property
    def current_window_handle(self) -> str:
        """Return the handle of the current window/tab."""
        return self._driver.current_window_handle

    # --- Element Finding Methods ---

    def _wrap_element(self, selenium_element) -> Element:
        """Wrap a Selenium WebElement in an Iridium Element."""
        return Element(selenium_element)

    def _wrap_elements(self, selenium_elements) -> List[Element]:
        """Wrap a list of Selenium WebElements in Iridium Elements."""
        return [Element(el) for el in selenium_elements]

    def find_element_by_id(self, id_value: str) -> Element:
        """Find an element by its ID attribute."""
        return self._wrap_element(self._driver.find_element(By.ID, id_value))

    def find_elements_by_id(self, id_value: str) -> List[Element]:
        """Find all elements by their ID attribute."""
        return self._wrap_elements(self._driver.find_elements(By.ID, id_value))

    def find_element_by_name(self, name: str) -> Element:
        """Find an element by its name attribute."""
        return self._wrap_element(self._driver.find_element(By.NAME, name))

    def find_elements_by_name(self, name: str) -> List[Element]:
        """Find all elements by their name attribute."""
        return self._wrap_elements(self._driver.find_elements(By.NAME, name))

    def find_element_by_class(self, class_name: str) -> Element:
        """Find an element by its CSS class name."""
        return self._wrap_element(self._driver.find_element(By.CLASS_NAME, class_name))

    def find_elements_by_class(self, class_name: str) -> List[Element]:
        """Find all elements by their CSS class name."""
        return self._wrap_elements(self._driver.find_elements(By.CLASS_NAME, class_name))

    def find_element_by_css(self, css_selector: str) -> Element:
        """Find an element by CSS selector."""
        return self._wrap_element(self._driver.find_element(By.CSS_SELECTOR, css_selector))

    def find_elements_by_css(self, css_selector: str) -> List[Element]:
        """Find all elements by CSS selector."""
        return self._wrap_elements(self._driver.find_elements(By.CSS_SELECTOR, css_selector))

    def find_element_by_xpath(self, xpath: str) -> Element:
        """Find an element by XPath expression."""
        return self._wrap_element(self._driver.find_element(By.XPATH, xpath))

    def find_elements_by_xpath(self, xpath: str) -> List[Element]:
        """Find all elements by XPath expression."""
        return self._wrap_elements(self._driver.find_elements(By.XPATH, xpath))

    def find_element_by_tag(self, tag_name: str) -> Element:
        """Find an element by its HTML tag name."""
        return self._wrap_element(self._driver.find_element(By.TAG_NAME, tag_name))

    def find_elements_by_tag(self, tag_name: str) -> List[Element]:
        """Find all elements by their HTML tag name."""
        return self._wrap_elements(self._driver.find_elements(By.TAG_NAME, tag_name))

    def find_element_by_text(self, text: str) -> Element:
        """Find an element by its exact visible text."""
        xpath = f".//*[normalize-space()='{text}']"
        return self.find_element_by_xpath(xpath)

    def find_element_by_partial_text(self, text: str) -> Element:
        """Find an element by partial visible text."""
        xpath = f".//*[contains(normalize-space(), '{text}')]"
        return self.find_element_by_xpath(xpath)

    # --- Wait Methods ---

    def wait_for_element_by_id(self, id_value: str, timeout: int = None) -> Element:
        """Wait for an element with the specified ID to appear."""
        timeout = timeout or self._implicit_wait
        wait = WebDriverWait(self._driver, timeout)
        element = wait.until(EC.presence_of_element_located((By.ID, id_value)))
        return self._wrap_element(element)

    def wait_for_element_by_xpath(self, xpath: str, timeout: int = None) -> Element:
        """Wait for an element matching the XPath to appear."""
        timeout = timeout or self._implicit_wait
        wait = WebDriverWait(self._driver, timeout)
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return self._wrap_element(element)

    def wait_for_element_by_text(self, text: str, timeout: int = None) -> Element:
        """Wait for an element with exact visible text to appear."""
        xpath = f".//*[normalize-space()='{text}']"
        return self.wait_for_element_by_xpath(xpath, timeout)

    def wait_for_element_to_disappear_by_id(
        self, id_value: str, timeout: int = None
    ) -> bool:
        """Wait for an element with the specified ID to disappear."""
        timeout = timeout or self._implicit_wait
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(EC.invisibility_of_element_located((By.ID, id_value)))

    def wait_for_element_to_disappear_by_xpath(
        self, xpath: str, timeout: int = None
    ) -> bool:
        """Wait for an element matching the XPath to disappear."""
        timeout = timeout or self._implicit_wait
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(EC.invisibility_of_element_located((By.XPATH, xpath)))

    # --- Window and Tab Management ---

    def open_new_tab(self, url: str = None) -> None:
        """Open a new browser tab and optionally navigate to a URL."""
        self._driver.execute_script("window.open('');")
        self._driver.switch_to.window(self._driver.window_handles[-1])
        if url:
            self.get(url)

    def switch_to_window(self, handle: str) -> None:
        """Switch to a specific window/tab by handle."""
        self._driver.switch_to.window(handle)

    def close_current_tab(self) -> None:
        """Close the current tab/window."""
        self._driver.close()

    def set_window_size(self, width: int, height: int) -> None:
        """Set browser window dimensions."""
        self._driver.set_window_size(width, height)

    def maximize_window(self) -> None:
        """Maximize the browser window."""
        self._driver.maximize_window()

    def minimize_window(self) -> None:
        """Minimize the browser window."""
        self._driver.minimize_window()

    def fullscreen_window(self) -> None:
        """Enter fullscreen mode."""
        self._driver.fullscreen_window()

    # --- Screenshots ---

    def take_screenshot(self, filename: str) -> bool:
        """
        Capture a screenshot of the current viewport.

        Args:
            filename: Path to save the screenshot.

        Returns:
            True if successful, False otherwise.
        """
        try:
            self._driver.save_screenshot(filename)
            logger.info(f"Screenshot saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
            return False

    # --- JavaScript Execution ---

    def execute_script(self, script: str, *args) -> object:
        """
        Execute JavaScript in the current browser context.

        Args:
            script: JavaScript code to execute.
            *args: Arguments to pass to the script.

        Returns:
            The result of the script execution.
        """
        return self._driver.execute_script(script, *args)

    # --- Cookie Management ---

    def add_cookie(self, cookie_dict: dict) -> None:
        """Add a cookie to the current session."""
        self._driver.add_cookie(cookie_dict)

    def get_cookie(self, name: str) -> Optional[dict]:
        """Get a specific cookie by name."""
        return self._driver.get_cookie(name)

    def get_cookies(self) -> List[dict]:
        """Get all cookies for the current domain."""
        return self._driver.get_cookies()

    def delete_cookie(self, name: str) -> None:
        """Delete a cookie by name."""
        self._driver.delete_cookie(name)

    def delete_all_cookies(self) -> None:
        """Delete all cookies."""
        self._driver.delete_all_cookies()

    # --- Utility ---

    def scroll_to_bottom(self) -> None:
        """Scroll to the bottom of the page."""
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self) -> None:
        """Scroll to the top of the page."""
        self.execute_script("window.scrollTo(0, 0);")

    def get_log(self, log_type: str = "browser") -> List[dict]:
        """
        Get browser logs.

        Args:
            log_type: Type of log to retrieve (browser, driver, performance).

        Returns:
            List of log entries.
        """
        return self._driver.get_log(log_type)
