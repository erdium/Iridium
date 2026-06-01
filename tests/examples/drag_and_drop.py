"""
Drag and Drop Example

Demonstrates:
- Dragging an element to a target location
"""

from iridium import Browser


def main():
    with Browser() as browser:
        browser.get("https://the-internet.herokuapp.com/drag_and_drop")

        # Locate the source and target elements
        column_a = browser.find_element_by_id("column-a")
        column_b = browser.find_element_by_id("column-b")

        print(f"Before drag: Column A = '{column_a.text}', Column B = '{column_b.text}'")

        # Drag column A onto column B
        column_a.drag_and_drop(column_b)

        # Verify the swap
        column_a = browser.find_element_by_id("column-a")
        column_b = browser.find_element_by_id("column-b")
        print(f"After drag:  Column A = '{column_a.text}', Column B = '{column_b.text}'")


if __name__ == "__main__":
    main()
