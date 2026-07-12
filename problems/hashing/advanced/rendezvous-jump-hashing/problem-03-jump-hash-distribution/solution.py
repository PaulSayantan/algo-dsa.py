"""Jump Consistent Hash — bucket distribution over several keys."""
from typing import List  # noqa: F401


class Solution:
    def jumpConsistentHash(self, key: int, num_buckets: int) -> int:
        # TODO: canonical jump-hash LCG (constant 2862933555777941757)
        pass

    def buckets(self, keys: List[int], num_buckets: int) -> List[int]:
        # TODO: return the bucket each key maps to
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.buckets([10, 20, 30, 40, 50], 8))  # expected: [7, 0, 3, 4, 2]
    print(sol.buckets([1, 2, 3, 4, 5, 6, 7, 8], 4))  # expected: [0, 3, 3, 1, 1, 2, 0, 0]
