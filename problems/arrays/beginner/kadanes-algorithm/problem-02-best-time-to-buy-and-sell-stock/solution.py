from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Return the maximum profit from a single buy-then-sell transaction.

        Args:
            prices: A list where ``prices[i]`` is the stock price on day ``i``.

        Returns:
            The maximum achievable profit, or ``0`` if no profitable
            buy-before-sell transaction exists.

        Example:
            >>> Solution().maxProfit([7, 1, 5, 3, 6, 4])
            5
        """
        # TODO: implement using Kadane's Algorithm on consecutive price differences
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # expected: 5
    print(sol.maxProfit([7, 6, 4, 3, 1]))     # expected: 0
