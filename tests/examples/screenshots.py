"""
Screenshot Capture Example

Demonstrates:
- Full viewport screenshots
- Individual element screenshots
"""

import os
from iridium import Browser


def main():
    # Create screenshots directory if it doesn't exist
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    with Browser() as browser:
        browser.get("https://www.python.org")

        # Take a viewport screenshot
        viewport_path = os.path.join(screenshots_dir, "python_org_viewport.png")
        browser.take_screenshot(viewport_path)
        print(f"Viewport screenshot saved: {viewport_path}")

        # Take a screenshot of a specific element
        logo = browser.find_element_by_css(".python-logo")
        element_path = os.path.join(screenshots_dir, "python_logo.png")
        logo.screenshot(element_path)
        print(f"Element screenshot saved: {element_path}")

        print("\nScreenshots captured successfully.")


if __name__ == "__main__":
    main()
