"""
Pytest configuration and shared fixtures.
"""

import pytest
import os
import tempfile


@pytest.fixture(scope="function")
def temp_dir():
    """Create a temporary directory for test artifacts."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture(scope="session")
def test_data_dir():
    """Return path to test data directory."""
    return os.path.join(os.path.dirname(__file__), "data")


def pytest_configure(config):
    """Add custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "requires_browser: marks tests that need a real browser"
    )
