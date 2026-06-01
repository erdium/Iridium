# Iridium

[![PyPI version](https://badge.fury.io/py/iridium.svg)](https://badge.fury.io/py/iridium)
[![Python Versions](https://img.shields.io/pypi/pyversions/iridium.svg)](https://pypi.org/project/iridium/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/iridium)](https://pepy.tech/project/iridium)
[![Documentation Status](https://readthedocs.org/projects/iridium/badge/?version=latest)](https://iridium.readthedocs.io/en/latest/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**A simple, elegant, and powerful wrapper around Selenium WebDriver.**

[Documentation](#documentation) |
[Installation](#installation) |
[Quick Start](#quick-start) |
[Features](#features) |
[API Reference](#api-reference) |
[Examples](#examples) |
[Contributing](#contributing)

---

## About

Iridium is a high-level Python library designed to simplify browser automation with Selenium WebDriver. Named after one of the most durable and corrosion-resistant metals on Earth, it provides a reliable, fast, and intuitive interface for web automation, testing, and scraping.

### Why Iridium?

- **Less code, more action** -- accomplish complex tasks with minimal boilerplate.
- **Smart waiting** -- built-in automatic element waits instead of unreliable `time.sleep()` calls.
- **Resilience** -- automatic retries and graceful exception handling out of the box.
- **Enhanced element location** -- find elements by XPath, CSS, visible text, partial text, and attributes with a clean API.
- **Debugging tools** -- screenshots, logging, and network monitoring built in.
- **Cross-browser support** -- Chrome, Firefox, Safari, Edge, and Opera.
- **Human-readable code** -- your test scripts read like plain instructions, not machine code.

---

## Installation

### Prerequisites

Python 3.7 or higher is required.

### Basic Installation

```bash
pip install iridium
```

### Install with Browser-Specific Drivers

```bash
pip install iridium[chrome]
pip install iridium[firefox]
pip install iridium[all]
```

### WebDriver Setup

Iridium manages WebDriver binaries automatically using `webdriver-manager`. No manual setup is required for most users.

For manual installation, see the [WebDriver Installation Guide](https://iridium.readthedocs.io/en/latest/installation/#webdriver-setup).

### Verify Installation

```python
import iridium
print(iridium.__version__)
```

---

## Quick Start

A minimal working example:

```python
from iridium import Browser

with Browser() as browser:
    browser.get("https://www.google.com")
    browser.find_element_by_name("q").send_keys("Iridium Python")
    browser.find_element_by_name("q").submit()
    print(browser.title)
```

Full working scripts for common use cases are located in the **[examples/](examples/)** directory of this repository.

---

## Features

### Core Functionality

- Context manager support for automatic browser cleanup
- Automatic WebDriver binary management
- Implicit and explicit wait strategies
- Element search by multiple locator strategies
- Single and multiple element queries
- Human-friendly element interaction methods

### Element Interaction

- Click, double-click, right-click, and hover actions
- Text input with automatic clearing
- Form submission
- Drag and drop support
- Attribute and property access

### Browser Management

- Tab and window switching
- Window resizing, maximizing, minimizing, and fullscreen
- Cookie management (add, get, delete)
- LocalStorage and SessionStorage access via JavaScript execution
- Alert and popup handling

### Advanced Features

- Headless mode for CI/CD and server environments
- Proxy configuration
- Custom browser profiles
- Network performance logging
- Screenshot capture (full page, viewport, or specific element)
- Parallel execution support with threading

### Testing Integration

- Seamless integration with `unittest` and `pytest`
- Page Object pattern support
- Automatic screenshot on failure
- Customizable timeouts per operation

---

## Examples

Complete, runnable examples are maintained in the **[examples/](examples/)** directory of this repository. Topics covered include:

| File | Description |
|------|-------------|
| `examples/basic_usage.py` | Browser setup, navigation, element search, and text input |
| `examples/waiting.py` | Smart waits, custom conditions, and element disappearance |
| `examples/screenshots.py` | Full page, viewport, and element screenshot capture |
| `examples/forms.py` | Form filling, checkboxes, radio buttons, and dropdowns |
| `examples/tabs_and_windows.py` | Opening, switching, and closing browser tabs and windows |
| `examples/cookies_and_storage.py` | Cookie manipulation and localStorage interaction |
| `examples/drag_and_drop.py` | Drag and drop operations |
| `examples/headless.py` | Running in headless mode for CI/CD |
| `examples/proxy.py` | Proxy configuration and IP verification |
| `examples/web_scraping.py` | Multi-page data extraction and CSV export |
| `examples/parallel.py` | Concurrent execution across multiple URLs |
| `examples/unittest_integration.py` | Writing tests with unittest |
| `examples/pytest_integration.py` | Writing tests with pytest |

To run any example:

```bash
python examples/basic_usage.py
```

All examples include detailed inline comments explaining each step.

---

## API Reference

### Browser

The main entry point for all browser automation tasks.

```python
class Browser:
    def __init__(
        self,
        browser: str = "chrome",
        options: Options = None,
        implicit_wait: int = 10,
        driver_path: str = None,
        use_webdriver_manager: bool = True
    )
```

#### Methods

| Method | Description |
|--------|-------------|
| `get(url)` | Navigate to a URL |
| `find_element_by_id(id)` | Find element by ID |
| `find_element_by_name(name)` | Find element by name attribute |
| `find_element_by_class(class_name)` | Find element by CSS class |
| `find_element_by_css(selector)` | Find element by CSS selector |
| `find_element_by_xpath(xpath)` | Find element by XPath |
| `find_element_by_tag(tag)` | Find element by HTML tag |
| `find_element_by_text(text)` | Find element by exact visible text |
| `find_element_by_partial_text(text)` | Find element by partial visible text |
| `find_elements_by_*(...)` | Plural variants returning lists |
| `wait_for_element_by_id(id, timeout=10)` | Wait for element to appear |
| `wait_for_element_to_disappear_by_id(id, timeout=10)` | Wait for element to disappear |
| `open_new_tab(url)` | Open URL in a new browser tab |
| `take_screenshot(filename)` | Capture viewport screenshot |
| `execute_script(script)` | Execute arbitrary JavaScript |
| `add_cookie(cookie_dict)` | Add a browser cookie |
| `get_cookie(name)` | Get a specific cookie |
| `get_cookies()` | Get all cookies |
| `delete_cookie(name)` | Delete a cookie |
| `delete_all_cookies()` | Delete all cookies |
| `set_window_size(width, height)` | Set browser window dimensions |
| `maximize_window()` | Maximize browser window |
| `minimize_window()` | Minimize browser window |
| `fullscreen_window()` | Enter fullscreen mode |
| `quit()` | Close the browser and end the session |

### Element

Represents a DOM element returned by any `find_element_*` method.

```python
class Element:
    text: str
    tag_name: str
    location: dict
    size: dict
```

#### Methods

| Method | Description |
|--------|-------------|
| `click()` | Left-click the element |
| `double_click()` | Double-click the element |
| `right_click()` | Right-click the element |
| `hover()` | Hover the mouse over the element |
| `send_keys(*value)` | Type text into the element |
| `clear()` | Clear the element content |
| `submit()` | Submit a form element |
| `get_attribute(name)` | Get the value of an HTML attribute |
| `is_displayed()` | Check if the element is visible |
| `is_enabled()` | Check if the element is interactable |
| `screenshot(filename)` | Capture a screenshot of this element |
| `drag_and_drop(target)` | Drag this element onto another element |

### Wait Utilities

```python
from iridium.wait import until

element = until(
    lambda: browser.find_element_by_id("dynamic-content"),
    timeout=15,
    error_message="Dynamic content did not appear"
)
```

Full API documentation is available at [iridium.readthedocs.io](https://iridium.readthedocs.io/en/latest/api/).

---

## Best Practices

### Do This

- Use the context manager (`with Browser() as browser:`) to guarantee cleanup
- Prefer CSS selectors and `data-*` attributes over fragile XPath expressions
- Use `wait_for_element_*` instead of `time.sleep()`
- Organize repeated actions into Page Object classes
- Set appropriate timeouts based on your application performance

### Avoid This

- Hard-coded delays (`time.sleep(5)`) instead of smart waits
- Overly complex or deeply nested XPath expressions
- Manual `browser.quit()` calls without `try/finally` or context managers
- Ignoring exception handling for network-dependent operations

---

## Comparison

| Capability | Iridium | Selenium Raw | Playwright | Puppeteer |
|------------|---------|--------------|------------|-----------|
| Ease of use | High | Medium | High | Medium |
| Smart waits | Built-in | Manual only | Built-in | Built-in |
| Auto driver management | Yes | No | Yes | Yes |
| Cross-browser | All major | All major | All major | Chrome only |
| Python-native experience | Yes | Yes | Good | Via pyppeteer |
| Documentation quality | Excellent | Good | Good | Moderate |

---

## Testing the Library

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run all tests
pytest tests/

# Run tests with coverage
pytest --cov=iridium tests/

# Run a specific test file
pytest tests/test_browser.py

# Run a specific test case
pytest tests/test_browser.py::TestBrowser::test_find_element
```

---

## Contributing

Contributions are welcome and appreciated. Here is how you can help:

- **Report bugs** by opening issues with detailed descriptions and reproduction steps
- **Suggest features** by opening feature request issues
- **Improve documentation** -- every typo fix counts
- **Fix bugs** -- check issues labeled `good first issue`
- **Add examples** -- share useful scripts in the `examples/` directory

### Development Workflow

```bash
# Fork and clone the repository
git clone https://github.com/your-username/iridium.git
cd iridium

# Install development dependencies
pip install -e ".[dev]"

# Create a feature branch
git checkout -b feature/my-feature

# Make changes and run tests
pytest tests/

# Format code
black iridium/

# Commit and push
git commit -m "Add my feature"
git push origin feature/my-feature

# Open a Pull Request
```

### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Format code with [Black](https://github.com/psf/black)
- Add type hints to new functions
- Write tests for new functionality
- Update the changelog and documentation as needed

---

## License

MIT License. See the [LICENSE](LICENSE) file for full details.

---

## Acknowledgments

- [Selenium WebDriver](https://www.selenium.dev/) -- the foundation this library is built on
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager) -- automatic driver management
- All [contributors](https://github.com/iridium/iridium/graphs/contributors)

---

## Support

- **Documentation**: [iridium.readthedocs.io](https://iridium.readthedocs.io)
- **Issue Tracker**: [GitHub Issues](https://github.com/iridium/iridium/issues)
- **Source Code**: [GitHub Repository](https://github.com/iridium/iridium)
- **PyPI Package**: [pypi.org/project/iridium](https://pypi.org/project/iridium/)
- **Discussions**: [GitHub Discussions](https://github.com/iridium/iridium/discussions)

---

## Repository Structure

```
iridium/
├── examples/                  # Runnable example scripts
│   ├── basic_usage.py
│   ├── waiting.py
│   ├── screenshots.py
│   ├── forms.py
│   ├── tabs_and_windows.py
│   ├── cookies_and_storage.py
│   ├── drag_and_drop.py
│   ├── headless.py
│   ├── proxy.py
│   ├── web_scraping.py
│   ├── parallel.py
│   ├── unittest_integration.py
│   └── pytest_integration.py
├── iridium/                   # Library source code
│   ├── __init__.py
│   ├── browser.py
│   ├── element.py
│   └── wait.py
├── tests/                     # Test suite
│   ├── test_browser.py
│   ├── test_element.py
│   └── conftest.py
│                     
├── LICENSE
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── setup.py
```
```

This README is clean, professional, English-only, and explicitly points users to the `examples/` directory for all code samples without embedding them directly in the documentation file.
