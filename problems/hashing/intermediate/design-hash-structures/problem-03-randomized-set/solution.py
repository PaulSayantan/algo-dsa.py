"""Insert Delete GetRandom O(1) — LeetCode 380 (deterministic ops only)."""


class RandomizedSet:
    def __init__(self) -> None:
        # TODO: value->index map + dynamic array; swap-delete for O(1) removal
        pass

    def insert(self, val: int) -> bool:
        # TODO: return False if present, else add and return True
        pass

    def remove(self, val: int) -> bool:
        # TODO: swap with last, pop; return whether it was present
        pass

    def size(self) -> int:
        # TODO
        pass


if __name__ == "__main__":
    rs = RandomizedSet()
    print(rs.insert(1))  # expected: True
    print(rs.insert(1))  # expected: False
    print(rs.remove(2))  # expected: False
    print(rs.insert(2))  # expected: True
    print(rs.remove(1))  # expected: True
    print(rs.size())  # expected: 1
