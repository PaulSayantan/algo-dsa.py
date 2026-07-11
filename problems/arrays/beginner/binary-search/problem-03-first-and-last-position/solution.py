"""LeetCode 34 - Find First and Last Position of Element in Sorted Array.

Return the [first, last] indices of `target` in the non-decreasing list `nums`,
or [-1, -1] if it is absent.
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Find the first and last indices of `target`.

        Args:
            nums: A list of integers sorted in non-decreasing order (duplicates
                allowed).
            target: The integer value whose range of positions is sought.

        Returns:
            A two-element list [first_index, last_index]. If `target` is not
            present, returns [-1, -1].

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
