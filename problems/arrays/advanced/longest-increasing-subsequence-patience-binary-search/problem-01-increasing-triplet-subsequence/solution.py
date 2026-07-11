"""Increasing Triplet Subsequence (LeetCode 334).

Empty solution template — fill in the logic yourself.
"""
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """Return True iff nums contains a strictly increasing subsequence of length 3.

        Args:
            nums: The input integer array. Order matters; elements may repeat
                and may be negative.

        Returns:
            True if there exist indices i < j < k with
            nums[i] < nums[j] < nums[k], otherwise False.

        Example:
            >>> Solution().increasingTriplet([2, 1, 5, 0, 4, 6])
            True
            >>> Solution().increasingTriplet([5, 4, 3, 2, 1])
            False
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.increasingTriplet([1, 2, 3, 4, 5]))   # expected: True
    print(sol.increasingTriplet([5, 4, 3, 2, 1]))   # expected: False
    print(sol.increasingTriplet([2, 1, 5, 0, 4, 6]))  # expected: True
