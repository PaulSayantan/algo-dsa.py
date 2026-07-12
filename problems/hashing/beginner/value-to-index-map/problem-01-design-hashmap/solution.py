"""Design HashMap — LeetCode 706. Support put / get / remove over integer keys."""


class MyHashMap:
    def __init__(self) -> None:
        # TODO: bucket array; map key -> slot via key % capacity
        pass

    def put(self, key: int, value: int) -> None:
        # TODO
        pass

    def get(self, key: int) -> int:
        # TODO: return the value for key, or -1 if absent
        pass

    def remove(self, key: int) -> None:
        # TODO
        pass


if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))  # expected: 1
    print(obj.get(3))  # expected: -1
    obj.put(2, 1)
    print(obj.get(2))  # expected: 1
    obj.remove(2)
    print(obj.get(2))  # expected: -1
