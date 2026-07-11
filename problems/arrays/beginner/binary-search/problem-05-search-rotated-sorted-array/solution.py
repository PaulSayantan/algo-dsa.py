"""LeetCode 33 - Search in Rotated Sorted Array.

Return the index of `target` in a rotated ascending array of distinct integers,
or -1 if it is absent, in O(log n) time.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Search for `target` in a rotated sorted array.

        Args:
            nums: An ascending array of distinct integers, possibly rotated at
                an unknown pivot.
            target: The integer value to locate.

        Returns:
            The index of `target` within `nums`, or -1 if it is absent.

        Example:
            >>> Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))  # expected: 4
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))  # expected: -1
    print(sol.search([1], 0))                      # expected: -1
