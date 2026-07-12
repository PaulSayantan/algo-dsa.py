"""Build a queue by middle insertion — repeated pushMiddle final order.

Insert each value of nums into the front-middle slot (index len // 2) of an
initially empty queue, then return the final contents front-first.
"""
from typing import List


class Solution:
    def buildByMiddle(self, nums: List[int]) -> List[int]:
        # TODO: insert each value at index len // 2 of the current list
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.buildByMiddle([1, 2, 3, 4, 5]))  # expected: [2, 4, 5, 3, 1]
    print(sol.buildByMiddle([]))  # expected: []
    print(sol.buildByMiddle([7]))  # expected: [7]
    print(sol.buildByMiddle([1, 2, 3, 4]))  # expected: [2, 4, 3, 1]
    print(sol.buildByMiddle([10, 20, 30]))  # expected: [20, 30, 10]
