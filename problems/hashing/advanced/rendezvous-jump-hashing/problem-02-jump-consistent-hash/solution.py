"""Jump Consistent Hash — Lamping & Veach (2014)."""


class Solution:
    def jumpConsistentHash(self, key: int, num_buckets: int) -> int:
        # TODO: implement the canonical LCG algorithm with constant
        # 2862933555777941757 returning a bucket in [0, num_buckets)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.jumpConsistentHash(1, 10))  # expected: 6
    print(sol.jumpConsistentHash(1000, 10))  # expected: 9
    print(sol.jumpConsistentHash(1000, 11))  # expected: 9
    print(sol.jumpConsistentHash(0, 1))  # expected: 0
    print(sol.jumpConsistentHash(42, 16))  # expected: 2
