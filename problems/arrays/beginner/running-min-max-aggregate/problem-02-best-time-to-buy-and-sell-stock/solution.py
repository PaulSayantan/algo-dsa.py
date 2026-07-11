from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Return the maximum profit from a single buy-then-sell transaction.

        Args:
            prices: prices[i] is the stock price on day i.

        Returns:
            The maximum achievable profit (buy day must precede sell day).
            Returns 0 if no profitable transaction exists.

        Example:
            >>> Solution().maxProfit([7, 1, 5, 3, 6, 4])
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # expected: 5
    print(sol.maxProfit([7, 6, 4, 3, 1]))     # expected: 0
    print(sol.maxProfit([2, 4, 1]))           # expected: 2
