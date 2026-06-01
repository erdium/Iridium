"""
Wait utilities for custom wait conditions.
"""

import time
import logging
from typing import Callable, Optional, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")


def until(
    condition: Callable[[], T],
    timeout: int = 10,
    poll_frequency: float = 0.5,
    error_message: Optional[str] = None,
) -> T:
    """
    Wait until a condition function returns a truthy value.

    Repeatedly calls the condition function until it returns a truthy value
    or the timeout is reached.

    Args:
        condition: A callable that returns a value. Waiting continues
                   until the return value is truthy.
        timeout: Maximum time to wait in seconds.
        poll_frequency: How often to check the condition in seconds.
        error_message: Custom error message if the wait times out.

    Returns:
        The first truthy value returned by the condition function.

    Raises:
        TimeoutError: If the condition does not become truthy within the timeout.

    Example:
        ```python
        from iridium.wait import until

        element = until(
            lambda: browser.find_element_by_id("dynamic-content"),
            timeout=15,
            error_message="Dynamic content did not appear"
        )
      """
        start_time = time.time()
last_exception = None

while True:
try:
result = condition()
if result:
logger.debug(f"Wait condition satisfied after {time.time() - start_time:.2f}s")
return result
except Exception as e:
last_exception = e

elapsed = time.time() - start_time
if elapsed >= timeout:
if error_message:
message = f"{error_message} (waited {elapsed:.2f}s)"
else:
message = f"Condition not met after {elapsed:.2f}s"
if last_exception:
message += f" | Last exception: {last_exception}"
logger.error(message)
raise TimeoutError(message)

time.sleep(poll_frequency)
