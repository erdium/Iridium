"""
Smart Waiting Example

Demonstrates different wait strategies:
- Waiting for elements to appear
- Waiting for elements to disappear
- Custom wait conditions
"""

from iridium import Browser
from iridium.wait import until


def main():
    with Browser() as browser:
        # Navigate to a page with dynamic content
        browser.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # Click the Start button
        start_button = browser.find_element_by_css("#start button")
        start_button.click()

        # Wait for the "Hello World!" text to appear (max 10 seconds)
        print("Waiting for content to load...")
        hello_element = browser.wait_for_element_by_text("Hello World!", timeout=10)
        print(f"Content loaded: {hello_element.text}")

        # Example of a custom wait condition
        browser.get("https://the-internet.herokuapp.com/dynamic_controls")

        # Click the checkbox and then remove it
        checkbox = browser.find_element_by_css("#checkbox input")
        checkbox.click()

        remove_button = browser.find_element_by_css("#checkbox-example button")
        remove_button.click()

        # Wait for the checkbox to disappear
        print("Waiting for checkbox to disappear...")
        browser.wait_for_element_to_disappear_by_id("checkbox", timeout=10)
        print("Checkbox removed successfully.")


if __name__ == "__main__":
    main()
