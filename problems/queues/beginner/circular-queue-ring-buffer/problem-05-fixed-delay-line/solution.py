"""Fixed-Delay Line — return the value pushed `delay` steps ago via a ring buffer."""


class DelayLine:
    def __init__(self, delay: int, fill: int = 0) -> None:
        # TODO: fixed-size buffer of `delay` slots seeded with fill, and head = 0
        ...

    def push(self, x: int) -> int:
        # TODO: read the slot at head (value from `delay` steps ago), overwrite it
        #       with x, advance head as (head + 1) % delay, and return the old value
        ...


if __name__ == "__main__":
    dl = DelayLine(3)
    print(dl.push(10))  # expected: 0
    print(dl.push(20))  # expected: 0
    print(dl.push(30))  # expected: 0
    print(dl.push(40))  # expected: 10
    print(dl.push(50))  # expected: 20

    d1 = DelayLine(1)
    print(d1.push(7))  # expected: 0
    print(d1.push(8))  # expected: 7
    print(d1.push(9))  # expected: 8

    df = DelayLine(3, -1)
    print(df.push(1))  # expected: -1
    print(df.push(4))  # expected: -1
    print(df.push(9))  # expected: -1
    print(df.push(16))  # expected: 1
    print(df.push(25))  # expected: 4
