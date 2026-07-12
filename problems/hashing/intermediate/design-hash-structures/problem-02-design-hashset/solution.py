"""Design HashSet — LeetCode 705."""


class MyHashSet:
    def __init__(self) -> None:
        # TODO: bucket array with modulo hashing
        pass

    def add(self, key: int) -> None:
        # TODO
        pass

    def contains(self, key: int) -> bool:
        # TODO
        pass

    def remove(self, key: int) -> None:
        # TODO
        pass


if __name__ == "__main__":
    s = MyHashSet()
    s.add(1)
    s.add(2)
    print(s.contains(1))  # expected: True
    print(s.contains(3))  # expected: False
    s.add(2)
    print(s.contains(2))  # expected: True
    s.remove(2)
    print(s.contains(2))  # expected: False
