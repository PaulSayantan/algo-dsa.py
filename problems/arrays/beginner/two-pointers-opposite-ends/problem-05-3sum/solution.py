"""3Sum — LeetCode 15.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Return all unique triplets that sum to zero.

        Args:
            nums: A list of integers.

        Returns:
            A list of unique triplets [a, b, c] with a + b + c == 0. No two
            returned triplets represent the same multiset of values.

        Example:
            >>> Solution().threeSum([-1, 0, 1, 2, -1, -4])
            [[-1, -1, 2], [-1, 0, 1]]
        """
        # TODO: implement using two pointers (opposite ends)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # expected: [[-1, -1, 2], [-1, 0, 1]]
    print(sol.threeSum([0, 1, 1]))              # expected: []
    print(sol.threeSum([0, 0, 0]))              # expected: [[0, 0, 0]]
