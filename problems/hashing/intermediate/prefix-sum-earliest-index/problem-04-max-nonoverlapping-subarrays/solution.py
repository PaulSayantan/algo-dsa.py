"""Maximum Number of Non-Overlapping Subarrays With Sum Equals Target — LeetCode 1546."""
from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # TODO: greedily cut a subarray whenever cur-target was seen, then reset
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxNonOverlapping([1, 1, 1, 1, 1], 2))  # expected: 2
    print(sol.maxNonOverlapping([-1, 3, 5, 1, 4, 2, -9], 6))  # expected: 2
    print(sol.maxNonOverlapping([0, 0, 0], 0))  # expected: 3
