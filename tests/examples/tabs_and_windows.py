"""
Tabs and Windows Example

Demonstrates:
- Opening new tabs
- Switching between tabs
- Closing specific tabs
"""

from iridium import Browser
import time


def main():
    with Browser() as browser:
        # Open first page
        browser.get("https://www.python.org")
        print(f"First tab: {browser.title}")

        # Open a new tab with a different URL
        browser.open_new_tab("https://www.github.com")
        print(f"Second tab: {browser.title}")

        # Switch back to the first tab
        handles = browser.window_handles
        browser.switch_to_window(handles[0])
        print(f"Switched back to: {browser.title}")

        # Switch to the second tab again
        browser.switch_to_window(handles[1])
        print(f"Switched to: {browser.title}")

        time.sleep(2)  # Brief pause to observe


if __name__ == "__main__":
    main()
