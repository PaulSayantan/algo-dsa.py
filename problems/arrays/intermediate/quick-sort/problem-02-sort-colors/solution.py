"""LeetCode 75 - Sort Colors (Dutch National Flag / 3-way partition).

Sort an array of 0s, 1s, and 2s in place with constant extra space.
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Sort nums in place so all 0s precede all 1s precede all 2s.

        Do not return anything; modify nums in place.

        Args:
            nums: List whose values are each 0, 1, or 2.

        Returns:
            None. The list is mutated in place.

        Example:
            >>> a = [2, 0, 2, 1, 1, 0]
            >>> Solution().sortColors(a)
            >>> a
            [0, 0, 1, 1, 2, 2]
        """
        # TODO: implement
        # Hint: 3-way partition with pivot value 1.
        # low marks the end of the 0s region, high marks the start of the 2s
        # region, mid scans forward.
        pass


if __name__ == "__main__":
    sol = Solution()

    a = [2, 0, 2, 1, 1, 0]
    sol.sortColors(a)
    print(a)  # expected: [0, 0, 1, 1, 2, 2]

    b = [2, 0, 1]
    sol.sortColors(b)
    print(b)  # expected: [0, 1, 2]

    c = [0]
    sol.sortColors(c)
    print(c)  # expected: [0]
