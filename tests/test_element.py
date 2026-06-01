"""
Tests for the Element class.
"""

import pytest
from unittest.mock import Mock, MagicMock

from iridium import Element


@pytest.fixture
def mock_selenium_element():
    """Create a mock Selenium WebElement."""
    element = MagicMock()
    element.text = "Test Element"
    element.tag_name = "div"
    element.location = {"x": 100, "y": 200}
    element.size = {"width": 300, "height": 50}
    return element


class TestElementProperties:
    """Tests for Element properties."""

    def test_text_property(self, mock_selenium_element):
        """Test that text property returns element text."""
        element = Element(mock_selenium_element)
        assert element.text == "Test Element"

    def test_tag_name_property(self, mock_selenium_element):
        """Test that tag_name property returns element tag."""
        element = Element(mock_selenium_element)
        assert element.tag_name == "div"

    def test_location_property(self, mock_selenium_element):
        """Test that location property returns element position."""
        element = Element(mock_selenium_element)
        assert element.location == {"x": 100, "y": 200}

    def test_size_property(self, mock_selenium_element):
        """Test that size property returns element dimensions."""
        element = Element(mock_selenium_element)
        assert element.size == {"width": 300, "height": 50}


class TestElementInteractions:
    """Tests for Element interaction methods."""

    def test_click(self, mock_selenium_element):
        """Test that click calls underlying element click."""
        element = Element(mock_selenium_element)
        element.click()
        mock_selenium_element.click.assert_called_once()

    def test_send_keys(self, mock_selenium_element):
        """Test that send_keys calls underlying element send_keys."""
        element = Element(mock_selenium_element)
        element.send_keys("hello")
        mock_selenium_element.send_keys.assert_called_once_with("hello")

    def test_clear(self, mock_selenium_element):
        """Test that clear calls underlying element clear."""
        element = Element(mock_selenium_element)
        element.clear()
        mock_selenium_element.clear.assert_called_once()

    def test_get_attribute(self, mock_selenium_element):
        """Test getting an element attribute."""
        mock_selenium_element.get_attribute.return_value = "value123"
        element = Element(mock_selenium_element)
        result = element.get_attribute("data-test")
        assert result == "value123"
        mock_selenium_element.get_attribute.assert_called_once_with("data-test")

    def test_is_displayed(self, mock_selenium_element):
        """Test checking if element is displayed."""
        mock_selenium_element.is_displayed.return_value = True
        element = Element(mock_selenium_element)
        assert element.is_displayed() is True

    def test_is_enabled(self, mock_selenium_element):
        """Test checking if element is enabled."""
        mock_selenium_element.is_enabled.return_value = True
        element = Element(mock_selenium_element)
        assert element.is_enabled() is True


class TestElementRepresentation:
    """Tests for Element string representation."""

    def test_repr(self, mock_selenium_element):
        """Test the __repr__ method."""
        element = Element(mock_selenium_element)
        repr_str = repr(element)
        assert "div" in repr_str
        assert "Test Element" in repr_str
