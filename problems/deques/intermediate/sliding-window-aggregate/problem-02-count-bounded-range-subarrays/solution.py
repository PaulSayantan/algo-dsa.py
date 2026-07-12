"""Count subarrays whose max - min <= limit (two-deque aggregate)."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def countSubarrays(self, nums: List[int], limit: int) -> int:
        # TODO: two monotonic deques; for each right, add (right - left + 1) valid subarrays
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubarrays([8, 2, 4, 7], 4))  # expected: 6
    print(sol.countSubarrays([1, 2, 3, 4], 1))  # expected: 7
    print(sol.countSubarrays([10, 1, 2, 4, 7, 2], 5))  # expected: 14
    print(sol.countSubarrays([4, 4, 4], 0))  # expected: 6
