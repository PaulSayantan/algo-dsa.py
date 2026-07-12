"""Binary Subarrays With Sum — LeetCode 930."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # TODO: prefix-sum frequency map over a 0/1 array
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubarraysWithSum([1, 0, 1, 0, 1], 2))  # expected: 4
    print(sol.numSubarraysWithSum([0, 0, 0, 0, 0], 0))  # expected: 15
    print(sol.numSubarraysWithSum([1, 1, 1], 0))  # expected: 0
