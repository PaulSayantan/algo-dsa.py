"""LeetCode 35 - Search Insert Position.

Return the index of `target`, or the index where it would be inserted to keep
`nums` sorted.
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Find the position of `target` or its correct insertion index.

        Args:
            nums: A list of distinct integers sorted in ascending order.
            target: The integer value to locate or insert.

        Returns:
            The index of `target` if present, otherwise the index at which it
            would be inserted to preserve ascending order (may equal
            len(nums)).

        Example:
            >>> Solution().searchInsert([1, 3, 5, 6], 2)
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))  # expected: 2
    print(sol.searchInsert([1, 3, 5, 6], 2))  # expected: 1
    print(sol.searchInsert([1, 3, 5, 6], 7))  # expected: 4
    print(sol.searchInsert([1, 3, 5, 6], 0))  # expected: 0
