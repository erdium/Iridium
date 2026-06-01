"""
Unittest Integration Example

Demonstrates:
- Writing browser tests with the unittest framework
- Using setUp/tearDown for browser lifecycle
- Making assertions on page content
"""

import unittest
from iridium import Browser


class TestPythonOrg(unittest.TestCase):
    """Tests for python.org website."""

    @classmethod
    def setUpClass(cls):
        """Set up browser once for all tests."""
        cls.browser = Browser()
        cls.browser.get("https://www.python.org")

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests."""
        cls.browser.quit()

    def test_page_title(self):
        """Test that the page title contains 'Python'."""
        self.assertIn("Python", self.browser.title)

    def test_search_functionality(self):
        """Test the search box is present and functional."""
        search_input = self.browser.find_element_by_name("q")
        self.assertTrue(search_input.is_displayed())

    def test_navigation_links_exist(self):
        """Test that navigation links are present."""
        nav_links = self.browser.find_elements_by_css("nav a")
        self.assertGreater(len(nav_links), 0)


if __name__ == "__main__":
    unittest.main()
