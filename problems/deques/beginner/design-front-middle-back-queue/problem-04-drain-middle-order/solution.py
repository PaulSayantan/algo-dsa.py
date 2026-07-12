"""Drain a queue from the middle — repeated popMiddle order.

Repeatedly remove the front-middle element (index (len - 1) // 2) until empty,
returning the removed values in removal order.
"""
from typing import List


class Solution:
    def drainMiddle(self, nums: List[int]) -> List[int]:
        # TODO: repeatedly pop index (len - 1) // 2 and collect the values
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.drainMiddle([1, 2, 3, 4, 5]))  # expected: [3, 2, 4, 1, 5]
    print(sol.drainMiddle([]))  # expected: []
    print(sol.drainMiddle([10]))  # expected: [10]
    print(sol.drainMiddle([1, 2, 3, 4]))  # expected: [2, 3, 1, 4]
    print(sol.drainMiddle([5, 6, 7]))  # expected: [6, 5, 7]
