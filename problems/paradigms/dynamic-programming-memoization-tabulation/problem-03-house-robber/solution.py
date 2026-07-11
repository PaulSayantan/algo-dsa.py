"""House Robber — LeetCode 198.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """Return the maximum money robbable without taking two adjacent houses.

        Args:
            nums: Money stashed in each house; nums[i] >= 0. Length 1..100.

        Returns:
            The maximum total money obtainable such that no two chosen indices
            are adjacent.

        Example:
            >>> Solution().rob([2, 7, 9, 3, 1])
            12
        """
        # TODO: implement using memoization (top-down) or tabulation (bottom-up).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))     # expected: 4
    print(sol.rob([2, 7, 9, 3, 1]))  # expected: 12
    print(sol.rob([5]))              # expected: 5
