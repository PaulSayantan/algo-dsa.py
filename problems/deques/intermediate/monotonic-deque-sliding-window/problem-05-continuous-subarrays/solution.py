"""Continuous Subarrays — LeetCode 2762."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # TODO: two monotonic deques; shrink left while max - min > 2, add (right-left+1)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.continuousSubarrays([5, 4, 2, 4]))  # expected: 8
    print(sol.continuousSubarrays([1, 2, 3]))  # expected: 6
    print(sol.continuousSubarrays([10]))  # expected: 1
    print(sol.continuousSubarrays([1, 4, 7, 10]))  # expected: 4
