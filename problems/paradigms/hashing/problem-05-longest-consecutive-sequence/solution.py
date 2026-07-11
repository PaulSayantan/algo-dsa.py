"""Longest Consecutive Sequence — empty solution template.

Fill in the body of `longestConsecutive` using a hash set for O(1) lookups.
Target complexity: O(n) time.
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Return the length of the longest run of consecutive integers in `nums`.

        Args:
            nums: Unsorted list of integers (may contain duplicates, may be empty).

        Returns:
            The length of the longest sequence of consecutive integers that can be
            formed from the values present in `nums`.

        Example:
            >>> Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))          # expected: 4
    print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # expected: 9
    print(sol.longestConsecutive([]))                              # expected: 0
