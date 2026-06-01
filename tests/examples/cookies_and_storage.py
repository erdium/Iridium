"""
Cookies and Storage Example

Demonstrates:
- Adding and retrieving cookies
- Deleting cookies
- Working with localStorage via JavaScript
"""

from iridium import Browser


def main():
    with Browser() as browser:
        browser.get("https://httpbin.org/cookies")

        # Add a cookie
        browser.add_cookie({"name": "user_session", "value": "abc123xyz"})
        browser.add_cookie({"name": "theme", "value": "dark"})

        # Get all cookies
        all_cookies = browser.get_cookies()
        print("All cookies:")
        for cookie in all_cookies:
            print(f"  {cookie['name']} = {cookie['value']}")

        # Get a specific cookie
        session_cookie = browser.get_cookie("user_session")
        if session_cookie:
            print(f"\nSession cookie: {session_cookie['value']}")

        # Delete a cookie
        browser.delete_cookie("theme")
        print("\nDeleted 'theme' cookie.")

        # Verify deletion
        remaining = browser.get_cookies()
        print(f"Remaining cookies: {len(remaining)}")

        # Work with localStorage
        browser.get("https://example.com")
        browser.execute_script("localStorage.setItem('app_version', '2.0.1');")
        version = browser.execute_script("return localStorage.getItem('app_version');")
        print(f"\nlocalStorage 'app_version': {version}")


if __name__ == "__main__":
    main()
