"""
Parallel Execution Example

Demonstrates:
- Running multiple browser instances concurrently
- Using ThreadPoolExecutor for parallel tasks
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from iridium import Browser


def fetch_page_info(url):
    """
    Open a URL and return page information.

    Args:
        url: The URL to fetch.

    Returns:
        A dictionary with URL, title, and status.
    """
    try:
        with Browser() as browser:
            browser.get(url)
            return {
                "url": url,
                "title": browser.title,
                "status": "success",
            }
    except Exception as e:
        return {
            "url": url,
            "title": None,
            "status": f"error: {e}",
        }


def main():
    urls = [
        "https://www.python.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.wikipedia.org",
    ]

    print(f"Fetching {len(urls)} URLs in parallel...\n")

    results = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(fetch_page_info, url): url for url in urls}

        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(f"  {result['url']}: {result['status']}")

    print(f"\nCompleted. {len(results)} results collected.")


if __name__ == "__main__":
    main()
