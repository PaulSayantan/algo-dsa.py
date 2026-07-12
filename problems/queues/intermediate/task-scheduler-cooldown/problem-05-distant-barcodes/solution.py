"""Distant Barcodes — LeetCode 1054."""
from typing import List  # noqa: F401
from collections import Counter  # noqa: F401


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # TODO: most-frequent-first, fill even indices then odd (one-slot cooldown)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rearrangeBarcodes([1, 1, 1, 2, 2, 2]))  # expected: [1, 2, 1, 2, 1, 2]
    print(sol.rearrangeBarcodes([1, 1, 1, 1, 2, 2, 3, 3]))  # expected: [1, 2, 1, 2, 1, 3, 1, 3]
    print(sol.rearrangeBarcodes([2, 2, 1, 3]))  # expected: [2, 1, 2, 3]
