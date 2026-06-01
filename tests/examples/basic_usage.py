"""
Basic Usage Example

Demonstrates fundamental Iridium operations:
- Browser initialization and navigation
- Element finding and text input
- Page title and source access
- Context manager usage
"""

from iridium import Browser


def main():
    # Using context manager ensures browser is closed automatically
    with Browser() as browser:
        # Navigate to a URL
        browser.get("https://www.google.com")

        # Find the search box by name attribute and type a query
        search_box = browser.find_element_by_name("q")
        search_box.send_keys("Iridium Python library")

        # Submit the search form
        search_box.submit()

        # Print the page title after search
        print(f"Page title: {browser.title}")

        # Find all search result headings
        results = browser.find_elements_by_css("h3")
        print(f"\nFound {len(results)} search results:")
        for i, result in enumerate(results[:5], 1):
            if result.text:
                print(f"  {i}. {result.text}")


if __name__ == "__main__":
    main()
