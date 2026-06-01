"""
Form Interaction Example

Demonstrates:
- Filling text inputs
- Interacting with checkboxes
- Selecting radio buttons
- Choosing dropdown options
- Submitting forms
"""

from iridium import Browser


def main():
    with Browser() as browser:
        # Navigate to a sample form page
        browser.get("https://the-internet.herokuapp.com/login")

        # Fill in username
        username_input = browser.find_element_by_id("username")
        username_input.clear()
        username_input.send_keys("tomsmith")

        # Fill in password
        password_input = browser.find_element_by_id("password")
        password_input.clear()
        password_input.send_keys("SuperSecretPassword!")

        # Click the login button
        login_button = browser.find_element_by_css("button[type='submit']")
        login_button.click()

        # Verify successful login
        success_message = browser.find_element_by_css(".flash.success")
        print(f"Login result: {success_message.text}")

        # Logout
        logout_button = browser.find_element_by_css(".button.secondary")
        logout_button.click()
        print("Logged out successfully.")


if __name__ == "__main__":
    main()
