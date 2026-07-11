"""Maximum Ice Cream Bars — LeetCode 1833.

Buy as many ice cream bars as possible with a fixed number of coins, choosing
the cheapest bars first.
"""
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """Return the maximum number of bars buyable with the given coins.

        Args:
            costs: Price of each ice cream bar. Each value is an integer in
                the range [1, 10**5].
            coins: Total coins available to spend (1 <= coins <= 10**8).

        Returns:
            The greatest number of bars that can be purchased without the total
            cost exceeding ``coins``.

        Example:
            >>> Solution().maxIceCream([1, 3, 2, 4, 1], 7)
            4
        """
        # TODO: implement using Counting Sort as the cheapest-first subroutine.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxIceCream([1, 3, 2, 4, 1], 7))       # expected: 4
    print(sol.maxIceCream([10, 6, 8, 7, 7, 8], 5))   # expected: 0
    print(sol.maxIceCream([1, 6, 3, 1, 2, 5], 20))   # expected: 6
