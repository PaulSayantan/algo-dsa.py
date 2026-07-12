"""Two Sum III - Data structure design — LeetCode 170."""
from collections import defaultdict  # noqa: F401


class TwoSum:
    def __init__(self) -> None:
        # TODO: frequency map of added numbers
        pass

    def add(self, number: int) -> None:
        # TODO
        pass

    def find(self, value: int) -> bool:
        # TODO: for each x, check value-x (mind x+x needing count>=2)
        pass


if __name__ == "__main__":
    ts = TwoSum()
    ts.add(1)
    ts.add(3)
    ts.add(5)
    print(ts.find(4))  # expected: True
    print(ts.find(7))  # expected: False
    print(ts.find(6))  # expected: True
    ts.add(3)
    print(ts.find(6))  # expected: True
