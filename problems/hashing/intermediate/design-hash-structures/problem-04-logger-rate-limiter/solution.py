"""Logger Rate Limiter — LeetCode 359."""


class Logger:
    def __init__(self) -> None:
        # TODO: message -> earliest next-allowed timestamp
        pass

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # TODO: allow only if 10s have passed since this message was last printed
        pass


if __name__ == "__main__":
    lg = Logger()
    print(lg.shouldPrintMessage(1, "foo"))  # expected: True
    print(lg.shouldPrintMessage(2, "bar"))  # expected: True
    print(lg.shouldPrintMessage(3, "foo"))  # expected: False
    print(lg.shouldPrintMessage(8, "bar"))  # expected: False
    print(lg.shouldPrintMessage(11, "foo"))  # expected: True
