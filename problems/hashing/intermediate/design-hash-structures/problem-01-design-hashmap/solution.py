"""Design HashMap — LeetCode 706."""


class MyHashMap:
    def __init__(self) -> None:
        # TODO: bucket array + modulo hashing with separate chaining
        pass

    def put(self, key: int, value: int) -> None:
        # TODO
        pass

    def get(self, key: int) -> int:
        # TODO: return value or -1
        pass

    def remove(self, key: int) -> None:
        # TODO
        pass


if __name__ == "__main__":
    m = MyHashMap()
    m.put(1, 1)
    m.put(2, 2)
    print(m.get(1))  # expected: 1
    print(m.get(3))  # expected: -1
    m.put(2, 1)
    print(m.get(2))  # expected: 1
    m.remove(2)
    print(m.get(2))  # expected: -1
