"""Minimum Size Subarray Sum (LeetCode 209).

Fill in the body using the Sliding Window technique.
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Return the length of the shortest contiguous subarray with sum >= target.

        Args:
            target: The positive threshold the subarray sum must reach.
            nums: A list of positive integers.

        Returns:
            The minimal length of a contiguous subarray whose sum is >= target,
            or 0 if no such subarray exists.

        Example:
            >>> Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))          # expected: 2
    print(sol.minSubArrayLen(4, [1, 4, 4]))                    # expected: 1
    print(sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))    # expected: 0
