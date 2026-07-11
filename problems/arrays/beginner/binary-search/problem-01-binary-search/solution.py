"""LeetCode 704 - Binary Search.

Return the index of `target` in the ascending sorted list `nums`, or -1.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Search for `target` in a sorted array using binary search.

        Args:
            nums: A list of unique integers sorted in ascending order.
            target: The integer value to locate.

        Returns:
            The index of `target` within `nums`, or -1 if it is absent.

        Example:
            >>> Solution().search([-1, 0, 3, 5, 9, 12], 9)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))  # expected: 4
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))  # expected: -1
    print(sol.search([5], 5))                    # expected: 0
