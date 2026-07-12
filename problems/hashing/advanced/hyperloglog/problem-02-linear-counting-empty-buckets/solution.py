"""Linear counting: a bitmap of m buckets; distinct count relates to empties."""
from typing import List  # noqa: F401


class LinearCounter:
    def __init__(self, m: int = 10) -> None:
        # TODO: a length-m bitmap of zeros
        pass

    def add(self, x: int) -> None:
        # TODO: set the hashed bucket to 1
        pass

    def filled_buckets(self) -> int:
        # TODO: how many buckets are set
        pass

    def empty_buckets(self) -> int:
        # TODO: how many buckets are still zero
        pass


if __name__ == "__main__":
    lc = LinearCounter(10)
    lc.add(1)
    lc.add(2)
    lc.add(3)
    lc.add(8)
    print(lc.filled_buckets())  # expected: 4
    print(lc.empty_buckets())  # expected: 6
    lc.add(11)
    print(lc.filled_buckets())  # expected: 4
    print(lc.empty_buckets())  # expected: 6
