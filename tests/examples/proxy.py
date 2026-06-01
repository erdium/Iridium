"""
Proxy Configuration Example

Demonstrates:
- Configuring browser to use a proxy server
- Verifying the proxy is active
"""

from selenium import webdriver
from iridium import Browser


def main():
    # Example proxy configuration
    # Replace with your actual proxy details
    PROXY_HOST = "your-proxy-server.com"
    PROXY_PORT = "8080"

    options = webdriver.ChromeOptions()
    options.add_argument(f"--proxy-server={PROXY_HOST}:{PROXY_PORT}")

    with Browser(options=options) as browser:
        try:
            # Check current IP to verify proxy
            browser.get("https://api.ipify.org?format=json")
            body_text = browser.find_element_by_tag("body").text
            print(f"Current IP via proxy: {body_text}")
        except Exception as e:
            print(f"Could not verify proxy: {e}")
            print("Note: Replace proxy settings with valid credentials for testing.")


if __name__ == "__main__":
    main()
