# Contributing to Iridium

Thank you for your interest in contributing to Iridium. This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Code Style](#code-style)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Feature Requests](#feature-requests)

## Code of Conduct

All contributors are expected to treat others with respect. Harassment and offensive behavior are not tolerated.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/your-username/iridium.git
cd iridium
```

3. Add the upstream repository:

```bash
git remote add upstream https://github.com/iridium/iridium.git
```

## Development Setup

Create a virtual environment and install development dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

Install pre-commit hooks:

```bash
pre-commit install
```

## Making Changes

1. Create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
```

2. Make your changes, following the code style guidelines
3. Add or update tests as necessary
4. Update documentation if needed

## Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=iridium
```

Run a specific test file:

```bash
pytest tests/test_browser.py
```

Run tests with verbose output:

```bash
pytest -v
```

## Code Style

Follow PEP 8. Use Black for code formatting:

```bash
black iridium/
```

Add type hints to function signatures. Write docstrings for all public functions and classes using Google style or NumPy style.

## Pull Request Process

1. Update the CHANGELOG.md with your changes
2. Run the full test suite and ensure all tests pass
3. Push your branch to your fork
4. Submit a pull request to the `main` branch
5. Ensure your PR description clearly describes the problem and solution
6. Link any related issues in the PR description

Your PR will be reviewed by maintainers. Feedback or changes may be requested before merging.

## Reporting Bugs

When reporting a bug, please include:

- Your operating system and Python version
- Iridium version
- Selenium version
- Browser and browser version
- A minimal code example that reproduces the issue
- Expected behavior vs actual behavior
- Any relevant error messages or stack traces

## Feature Requests

Feature requests are welcome. When submitting a feature request, please explain:

- The use case or problem the feature solves
- How the feature would work from a user perspective
- Any potential drawbacks or alternatives considered
