# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.1] - 2024-01-15

### Fixed
- Resolved issue with implicit wait not being applied on browser initialization
- Fixed `wait_for_element_to_disappear_by_id` returning incorrect type
- Corrected WebDriver Manager import paths for newer versions

### Changed
- Improved error messages for unsupported browser types
- Updated documentation links in README

## [2.0.0] - 2023-12-01

### Added
- Full context manager support (`with Browser() as browser:`)
- `find_element_by_text()` and `find_element_by_partial_text()` methods
- `drag_and_drop()` method on Element class
- `scroll_to()` method on Element class
- `get_log()` method for browser log retrieval
- Parallel execution example in `examples/parallel.py`
- Cookie management methods: `add_cookie`, `get_cookie`, `get_cookies`, `delete_cookie`, `delete_all_cookies`
- `execute_script()` method for JavaScript execution
- `switch_to_window()` and `close_current_tab()` methods
- Proxy configuration example
- Unittest and pytest integration examples

### Changed
- **Breaking**: `Browser` initialization signature changed to accept keyword arguments
- **Breaking**: `find_element_*` methods now return `Element` objects instead of raw Selenium WebElements
- Improved documentation across all modules
- Refactored wait utilities into separate `wait` module
- Renamed `save_screenshot` to `take_screenshot` for consistency

### Removed
- Deprecated `get_element()` method (use `find_element_*` instead)
- Support for Python 3.6 (end of life)

## [1.2.0] - 2023-06-10

### Added
- `find_element_by_css()` and `find_elements_by_css()` methods
- `find_element_by_xpath()` and `find_elements_by_xpath()` methods
- Screenshot functionality for viewport and elements
- Basic wait utilities

### Fixed
- Browser not quitting properly when exception occurs during initialization
- Typo in error message for element not found

## [1.1.0] - 2023-03-20

### Added
- Firefox browser support
- Automatic WebDriver management via webdriver-manager
- `open_new_tab()` method

### Changed
- Default browser changed from Chrome to Chrome (no change, clarified in docs)

## [1.0.0] - 2023-01-15

### Added
- Initial release
- Basic browser automation with Chrome support
- Element finding by ID, name, class, and tag
- `click`, `send_keys`, `clear`, and `submit` element interactions
- Implicit wait configuration
- Basic README and documentation
