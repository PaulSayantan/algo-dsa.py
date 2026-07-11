"""Find First and Last Position of Element in Sorted Array (LeetCode 34).

Given a non-decreasing array and a target, return the first and last indices of
target, or [-1, -1] when target is absent.
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Return [first_index, last_index] of target, or [-1, -1] if absent.

        Args:
            nums: A list of integers sorted in non-decreasing order (may be empty).
            target: The value whose index range is requested.

        Returns:
            A two-element list [first, last] giving the smallest and largest
            indices where target occurs, or [-1, -1] if target is not present.

        Example:
            >>> Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
            [3, 4]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))  # expected: [3, 4]
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))  # expected: [-1, -1]
    print(sol.searchRange([], 0))                    # expected: [-1, -1]
