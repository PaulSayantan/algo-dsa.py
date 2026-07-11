"""Coin Change — LeetCode 322.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Return the fewest coins summing to amount, or -1 if impossible.

        Each coin denomination may be used an unlimited number of times.

        Args:
            coins: The available coin denominations (each >= 1).
            amount: The target total to make (0 <= amount <= 10**4).

        Returns:
            The minimum number of coins whose values sum to amount, or -1 if no
            combination reaches amount.

        Example:
            >>> Solution().coinChange([1, 2, 5], 11)
            3
        """
        # TODO: implement using memoization (top-down) or tabulation (bottom-up).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1, 2, 5], 11))  # expected: 3
    print(sol.coinChange([2], 3))         # expected: -1
    print(sol.coinChange([1], 0))         # expected: 0
