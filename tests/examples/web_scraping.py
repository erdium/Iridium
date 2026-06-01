"""
Web Scraping Example

Demonstrates:
- Multi-page data extraction
- Collecting structured data
- Exporting results to CSV
"""

import csv
import os
from iridium import Browser


def scrape_quotes(output_file="quotes.csv"):
    """
    Scrape quotes from quotes.toscrape.com across multiple pages.

    Args:
        output_file: Path to save the CSV output.
    """
    quotes_data = []

    with Browser() as browser:
        browser.get("https://quotes.toscrape.com/")
        page_num = 1

        while True:
            print(f"Scraping page {page_num}...")

            # Find all quote blocks on the current page
            quotes = browser.find_elements_by_class("quote")

            for quote in quotes:
                text = quote.find_element_by_class("text").text
                author = quote.find_element_by_class("author").text
                tags = [tag.text for tag in quote.find_elements_by_class("tag")]

                quotes_data.append({
                    "text": text,
                    "author": author,
                    "tags": ", ".join(tags),
                })

            # Try to go to the next page
            try:
                next_button = browser.find_element_by_css(".next > a")
                next_button.click()
                page_num += 1
            except Exception:
                # No more pages
                break

    # Save to CSV
    if quotes_data:
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
            writer.writeheader()
            writer.writerows(quotes_data)

        print(f"\nScraped {len(quotes_data)} quotes from {page_num} pages.")
        print(f"Data saved to: {os.path.abspath(output_file)}")
    else:
        print("No quotes were scraped.")


if __name__ == "__main__":
    scrape_quotes()
