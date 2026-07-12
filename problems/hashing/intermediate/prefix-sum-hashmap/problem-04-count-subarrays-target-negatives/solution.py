"""Count contiguous subarrays summing to target (negatives allowed)."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], target: int) -> int:
        # TODO: prefix-sum frequency map handles negatives (no sliding window)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubarrays([1, -1, 1, -1], 0))  # expected: 4
    print(sol.countSubarrays([-1, -1, 1], 0))  # expected: 1
    print(sol.countSubarrays([5, -5, 5, -5, 5], 5))  # expected: 6
