"""Search in Rotated Sorted Array (LeetCode 33).

Fill in `search` using the Search in Rotated Sorted Array technique.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Return the index of `target` in a rotated sorted array, or -1.

        Args:
            nums: An ascending array of distinct integers, possibly rotated at
                an unknown pivot.
            target: The value to locate.

        Returns:
            The index of `target` within `nums`, or -1 if it is absent.

        Example:
            >>> Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    solver = Solution()
    print(solver.search([4, 5, 6, 7, 0, 1, 2], 0))  # expected: 4
    print(solver.search([4, 5, 6, 7, 0, 1, 2], 3))  # expected: -1
    print(solver.search([1], 1))                     # expected: 0
