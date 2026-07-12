"""Maximum Sum of a Bounded-Range Subarray (two-deque variable window)."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def maxBoundedSum(self, nums: List[int], limit: int) -> int:
        # TODO: two monotonic deques + running window sum; shrink while max - min > limit
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxBoundedSum([1, 3, 6, 2, 4], 2))  # expected: 6
    print(sol.maxBoundedSum([8, 2, 4, 7], 4))  # expected: 11
    print(sol.maxBoundedSum([10, 1, 2, 4, 7, 2], 5))  # expected: 15
    print(sol.maxBoundedSum([3, 3, 3], 0))  # expected: 9
    print(sol.maxBoundedSum([5], 0))  # expected: 5
