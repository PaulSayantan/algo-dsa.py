"""Find Minimum in Rotated Sorted Array II (LeetCode 154).

Fill in `findMin` using the Search in Rotated Sorted Array technique, with a
tie-breaking rule for duplicates.
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Return the minimum element of a rotated sorted array with duplicates.

        Args:
            nums: A list that was sorted in ascending order and then rotated
                between 1 and n times. Duplicates are allowed.

        Returns:
            The smallest element in `nums`.

        Example:
            >>> Solution().findMin([2, 2, 2, 0, 1])
            0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    solver = Solution()
    print(solver.findMin([1, 3, 5]))        # expected: 1
    print(solver.findMin([2, 2, 2, 0, 1]))  # expected: 0
    print(solver.findMin([3, 3, 1, 3]))     # expected: 1
