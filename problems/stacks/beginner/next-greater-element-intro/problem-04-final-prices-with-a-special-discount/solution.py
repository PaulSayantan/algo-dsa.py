"""Final Prices With a Special Discount in a Shop — LeetCode 1475."""
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # TODO: stack of indices; when a price <= a waiting item's price arrives, it is that item's discount
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.finalPrices([8, 4, 6, 2, 3]))  # expected: [4, 2, 4, 2, 3]
    print(sol.finalPrices([1, 2, 3, 4, 5]))  # expected: [1, 2, 3, 4, 5]
    print(sol.finalPrices([10, 1, 1, 6]))  # expected: [9, 0, 1, 6]
    print(sol.finalPrices([7]))  # expected: [7]
