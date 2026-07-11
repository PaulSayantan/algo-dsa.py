"""Minimum Size Subarray Sum — empty solution template.

Fill in the body of `minSubArrayLen`. Do not hard-code answers.
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Return the minimal length of a contiguous subarray with sum >= target.

        Args:
            target: The positive integer sum threshold to reach or exceed.
            nums: A list of positive integers.

        Returns:
            The length of the shortest contiguous subarray whose sum is
            >= target, or 0 if no such subarray exists.

        Example:
            >>> Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
            2
        """
        # TODO: implement using a variable-size sliding window
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # expected: 2
    print(sol.minSubArrayLen(4, [1, 4, 4]))           # expected: 1
    print(sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # expected: 0
