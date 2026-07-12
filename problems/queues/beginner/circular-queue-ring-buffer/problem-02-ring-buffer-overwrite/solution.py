"""A fixed-capacity ring buffer that overwrites the oldest item when full."""
from typing import List  # noqa: F401


class RingBuffer:
    def __init__(self, capacity: int) -> None:
        # TODO: fixed buffer, head index, and current size
        pass

    def write(self, x: int) -> None:
        # TODO: write at the rear; if full, advance head (drop the oldest)
        pass

    def snapshot(self) -> List[int]:
        # TODO: return live elements from oldest to newest
        pass

    def size(self) -> int:
        # TODO
        pass


if __name__ == "__main__":
    rb = RingBuffer(3)
    rb.write(1)
    rb.write(2)
    print(rb.snapshot())  # expected: [1, 2]
    rb.write(3)
    print(rb.snapshot())  # expected: [1, 2, 3]
    print(rb.size())  # expected: 3
    rb.write(4)
    print(rb.snapshot())  # expected: [2, 3, 4]
    rb.write(5)
    print(rb.snapshot())  # expected: [3, 4, 5]
    print(rb.size())  # expected: 3
