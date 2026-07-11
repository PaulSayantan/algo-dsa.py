"""Find Minimum in Rotated Sorted Array (LeetCode 153).

Fill in `findMin` using the Search in Rotated Sorted Array technique.
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Return the minimum element of a rotated sorted array of unique values.

        Args:
            nums: A list that was sorted in ascending order and then rotated
                between 1 and n times. All elements are distinct.

        Returns:
            The smallest element in `nums` (the value at the rotation pivot).

        Example:
            >>> Solution().findMin([4, 5, 6, 7, 0, 1, 2])
            0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    solver = Solution()
    print(solver.findMin([3, 4, 5, 1, 2]))        # expected: 1
    print(solver.findMin([4, 5, 6, 7, 0, 1, 2]))  # expected: 0
    print(solver.findMin([11, 13, 15, 17]))       # expected: 11
