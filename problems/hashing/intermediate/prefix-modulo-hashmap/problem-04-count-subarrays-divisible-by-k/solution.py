"""Count subarrays with sum divisible by k."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def countDivisible(self, nums: List[int], k: int) -> int:
        # TODO: equal prefix remainders ⇒ divisible sum; count pairs
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countDivisible([2, 4, 6], 2))  # expected: 6
    print(sol.countDivisible([1, 2, 3, 4], 3))  # expected: 4
    print(sol.countDivisible([5, 10, 15], 5))  # expected: 6
