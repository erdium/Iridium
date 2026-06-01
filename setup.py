"""
Setup configuration for Iridium package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="iridium",
    version="2.0.1",
    author="Iridium Contributors",
    author_email="contributors@iridium.dev",
    description="A simple, elegant, and powerful wrapper around Selenium WebDriver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iridium/iridium",
    packages=find_packages(exclude=["tests", "examples", "docs"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "selenium>=4.0.0",
        "webdriver-manager>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
            "pre-commit>=3.0.0",
        ],
        "chrome": [
            "webdriver-manager[chrome]>=4.0.0",
        ],
        "firefox": [
            "webdriver-manager[firefox]>=4.0.0",
        ],
        "all": [
            "webdriver-manager[all]>=4.0.0",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/iridium/iridium/issues",
        "Source": "https://github.com/iridium/iridium",
        "Documentation": "https://iridium.readthedocs.io",
    },
)
