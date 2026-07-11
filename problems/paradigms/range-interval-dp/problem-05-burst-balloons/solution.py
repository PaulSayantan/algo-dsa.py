"""Burst Balloons (LeetCode 312).

Fill in the body of `maxCoins` using Range / Interval DP.
Hint: think about the balloon burst LAST inside each interval.
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """Return the maximum coins collectable by bursting all balloons.

        Args:
            nums: Balloon values; length n (1..300), each value in [0, 100].

        Returns:
            The maximum total coins, where bursting balloon i yields
            nums[i-1] * nums[i] * nums[i+1] with out-of-bounds treated as 1.

        Example:
            >>> Solution().maxCoins([3, 1, 5, 8])
            167
        """
        # TODO: pad with virtual 1s, then interval DP choosing the last-burst k
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxCoins([3, 1, 5, 8]))  # expected: 167
    print(sol.maxCoins([1, 5]))        # expected: 10
    print(sol.maxCoins([7]))           # expected: 7
