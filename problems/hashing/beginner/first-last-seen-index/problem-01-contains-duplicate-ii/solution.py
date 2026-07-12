"""Contains Duplicate II — LeetCode 219. Equal values within index distance k?"""
from typing import List  # noqa: F401


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # TODO: store each value's most recent index; check the gap on a repeat
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))  # expected: True
    print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))  # expected: True
    print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # expected: False
    print(sol.containsNearbyDuplicate([1, 2, 1], 0))  # expected: False
    print(sol.containsNearbyDuplicate([99, 99], 1))  # expected: True
