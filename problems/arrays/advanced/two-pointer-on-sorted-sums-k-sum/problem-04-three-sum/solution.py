"""3Sum (LeetCode 15).

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Return all unique triplets that sum to zero.

        Args:
            nums: List of integers (unsorted; you may sort in place).

        Returns:
            A list of triplets ``[a, b, c]`` with ``a + b + c == 0`` drawn from three
            distinct indices. The result must contain no duplicate triplets (same
            multiset of values). Order of triplets and of values within a triplet
            does not matter.

        Example:
            >>> Solution().threeSum([-1, 0, 1, 2, -1, -4])
            [[-1, -1, 2], [-1, 0, 1]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # expected: [[-1, -1, 2], [-1, 0, 1]]
    print(sol.threeSum([0, 1, 1]))              # expected: []
    print(sol.threeSum([0, 0, 0]))              # expected: [[0, 0, 0]]
