"""3Sum — LeetCode 15.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Return all unique triplets that sum to zero.

        A triplet uses three distinct indices i, j, k with
        nums[i] + nums[j] + nums[k] == 0. Triplets with the same set of values
        must appear at most once in the output.

        Args:
            nums: The integer array to search.

        Returns:
            A list of unique value-triplets (each a length-3 list) summing to 0.

        Example:
            >>> Solution().threeSum([-1, 0, 1, 2, -1, -4])
            [[-1, -1, 2], [-1, 0, 1]]
            >>> Solution().threeSum([0, 1, 1])
            []
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # expected: [[-1, -1, 2], [-1, 0, 1]]
    print(sol.threeSum([0, 1, 1]))               # expected: []
    print(sol.threeSum([0, 0, 0, 0]))            # expected: [[0, 0, 0]]
