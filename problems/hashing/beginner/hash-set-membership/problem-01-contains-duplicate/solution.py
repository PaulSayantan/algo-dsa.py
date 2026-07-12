"""Contains Duplicate — LeetCode 217."""
from typing import List  # noqa: F401


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # TODO: track seen values in a set; a repeat means a duplicate
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))  # expected: True
    print(sol.containsDuplicate([1, 2, 3, 4]))  # expected: False
    print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # expected: True
    print(sol.containsDuplicate([1]))  # expected: False
