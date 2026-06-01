"""
Element module - Represents a DOM element with simplified interaction methods.
"""

import logging
from typing import Optional, List

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

logger = logging.getLogger(__name__)


class Element:
    """
    A wrapper around Selenium WebElement with simplified interaction methods.

    Provides human-friendly methods for common element interactions including
    click, double-click, right-click, hover, drag and drop, and more.
    """

    def __init__(self, selenium_element: WebElement):
        """
        Initialize an Element wrapper.

        Args:
            selenium_element: A Selenium WebElement instance.
        """
        self._element = selenium_element

    @property
    def text(self) -> str:
        """Return the visible text of the element."""
        return self._element.text

    @property
    def tag_name(self) -> str:
        """Return the HTML tag name of the element."""
        return self._element.tag_name

    @property
    def location(self) -> dict:
        """Return the location of the element on the page."""
        return self._element.location

    @property
    def size(self) -> dict:
        """Return the dimensions of the element."""
        return self._element.size

    def click(self) -> None:
        """Perform a left-click on the element."""
        logger.debug(f"Clicking element: {self.tag_name}")
        self._element.click()

    def double_click(self) -> None:
        """Perform a double-click on the element."""
        logger.debug(f"Double-clicking element: {self.tag_name}")
        actions = ActionChains(self._element.parent)
        actions.double_click(self._element).perform()

    def right_click(self) -> None:
        """Perform a right-click on the element."""
        logger.debug(f"Right-clicking element: {self.tag_name}")
        actions = ActionChains(self._element.parent)
        actions.context_click(self._element).perform()

    def hover(self) -> None:
        """Hover the mouse cursor over the element."""
        logger.debug(f"Hovering over element: {self.tag_name}")
        actions = ActionChains(self._element.parent)
        actions.move_to_element(self._element).perform()

    def send_keys(self, *value) -> None:
        """
        Type text into the element.

        Args:
            *value: Text to type into the element.
        """
        logger.debug(f"Sending keys to element: {self.tag_name}")
        self._element.send_keys(*value)

    def clear(self) -> None:
        """Clear the content of the element."""
        logger.debug(f"Clearing element: {self.tag_name}")
        self._element.clear()

    def submit(self) -> None:
        """Submit a form element."""
        logger.debug(f"Submitting element: {self.tag_name}")
        self._element.submit()

    def get_attribute(self, name: str) -> Optional[str]:
        """
        Get the value of an HTML attribute.

        Args:
            name: The name of the attribute.

        Returns:
            The attribute value, or None if not present.
        """
        return self._element.get_attribute(name)

    def get_property(self, name: str) -> Optional[str]:
        """
        Get the value of a DOM property.

        Args:
            name: The name of the property.

        Returns:
            The property value, or None if not present.
        """
        return self._element.get_property(name)

    def is_displayed(self) -> bool:
        """Check if the element is visible on the page."""
        return self._element.is_displayed()

    def is_enabled(self) -> bool:
        """Check if the element is interactable."""
        return self._element.is_enabled()

    def is_selected(self) -> bool:
        """Check if the element is selected (for checkboxes, radio buttons)."""
        return self._element.is_selected()

    def screenshot(self, filename: str) -> bool:
        """
        Capture a screenshot of this specific element.

        Args:
            filename: Path to save the screenshot.

        Returns:
            True if successful, False otherwise.
        """
        try:
            self._element.screenshot(filename)
            logger.info(f"Element screenshot saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to take element screenshot: {e}")
            return False

    def drag_and_drop(self, target: "Element") -> None:
        """
        Drag this element and drop it onto a target element.

        Args:
            target: The target Element to drop onto.
        """
        logger.debug(f"Dragging element to target: {target.tag_name}")
        actions = ActionChains(self._element.parent)
        actions.drag_and_drop(self._element, target._element).perform()

    def scroll_to(self) -> None:
        """Scroll the page until this element is in view."""
        self._element.parent.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            self._element,
        )

    def __repr__(self) -> str:
        return f"Element(tag={self.tag_name}, text='{self.text[:50]}')"
