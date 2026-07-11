"""Search Insert Position (LeetCode 35).

Return the index of ``target`` in a sorted array of distinct integers, or the
index at which it would be inserted to keep the array sorted.
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Find the index of ``target`` or its insertion point.

        Args:
            nums: A list of distinct integers sorted in ascending order.
            target: The value to search for.

        Returns:
            The index of ``target`` if present; otherwise the index where it
            would be inserted so ``nums`` stays sorted. The result is always in
            the range ``[0, len(nums)]``.

        Example:
            >>> Solution().searchInsert([1, 3, 5, 6], 5)
            2
            >>> Solution().searchInsert([1, 3, 5, 6], 2)
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # Expected: 2
    print(sol.searchInsert([1, 3, 5, 6], 5))
    # Expected: 1
    print(sol.searchInsert([1, 3, 5, 6], 2))
    # Expected: 4
    print(sol.searchInsert([1, 3, 5, 6], 7))
