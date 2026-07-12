"""Logger Rate Limiter — LeetCode 359 (design, 10s per-message window)."""
from collections import deque  # noqa: F401


class Logger:
    def __init__(self) -> None:
        # TODO: queue of (timestamp, message) in the window + set of live messages
        pass

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # TODO: evict fronts with time <= timestamp - 10, then allow only if
        # `message` is not currently in the window
        pass


if __name__ == "__main__":
    lg = Logger()
    print(lg.shouldPrintMessage(1, "foo"))  # expected: True
    print(lg.shouldPrintMessage(2, "bar"))  # expected: True
    print(lg.shouldPrintMessage(3, "foo"))  # expected: False
    print(lg.shouldPrintMessage(8, "bar"))  # expected: False
    print(lg.shouldPrintMessage(11, "foo"))  # expected: True
    print(lg.shouldPrintMessage(12, "bar"))  # expected: True
