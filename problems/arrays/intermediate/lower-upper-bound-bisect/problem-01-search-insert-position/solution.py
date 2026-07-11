"""Search Insert Position (LeetCode 35).

Return the index of `target` in the sorted, distinct array `nums`, or the index
where it would be inserted to keep `nums` sorted.
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Return the index of target, or its insertion point if absent.

        Args:
            nums: A list of distinct integers sorted in ascending order.
            target: The value to locate or place.

        Returns:
            The index in [0, len(nums)] equal to the first position whose value
            is >= target (i.e. the lower bound of target).

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
