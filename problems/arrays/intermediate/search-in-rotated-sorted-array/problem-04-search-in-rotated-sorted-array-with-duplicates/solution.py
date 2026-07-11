"""Search in Rotated Sorted Array II (LeetCode 81).

Fill in `search` using the Search in Rotated Sorted Array technique, with a
guard for duplicates.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """Return whether `target` exists in a rotated sorted array with dupes.

        Args:
            nums: A non-decreasing array (duplicates allowed), rotated at an
                unknown pivot.
            target: The value to look for.

        Returns:
            True if `target` occurs anywhere in `nums`, otherwise False.

        Example:
            >>> Solution().search([2, 5, 6, 0, 0, 1, 2], 0)
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    solver = Solution()
    print(solver.search([2, 5, 6, 0, 0, 1, 2], 0))  # expected: True
    print(solver.search([2, 5, 6, 0, 0, 1, 2], 3))  # expected: False
    print(solver.search([1, 0, 1, 1, 1], 0))         # expected: True
