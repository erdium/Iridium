"""
Headless Browser Example

Demonstrates:
- Running browser in headless mode (no GUI)
- Suitable for CI/CD pipelines and servers
"""

from selenium import webdriver
from iridium import Browser


def main():
    # Configure Chrome options for headless mode
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Create browser with headless options
    with Browser(options=options) as browser:
        browser.get("https://www.python.org")

        print(f"Page title: {browser.title}")
        print(f"Current URL: {browser.current_url}")

        # Find and print the main heading
        heading = browser.find_element_by_css("h1.site-headline")
        print(f"Main heading: {heading.text}")

        # Count navigation links
        nav_links = browser.find_elements_by_css("nav a")
        print(f"Navigation links found: {len(nav_links)}")


if __name__ == "__main__":
    main()
