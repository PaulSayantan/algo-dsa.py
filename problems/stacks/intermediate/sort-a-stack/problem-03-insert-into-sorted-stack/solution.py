"""Insert a value into an already-sorted stack, keeping it sorted."""
from typing import List


class Solution:
    def sortedInsert(self, stack: List[int], x: int) -> List[int]:
        # TODO: pop tops greater than x aside, push x, then restore the popped tops
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortedInsert([1, 3, 5], 4))  # expected: [1, 3, 4, 5]
    print(sol.sortedInsert([1, 3, 5], 6))  # expected: [1, 3, 5, 6]
    print(sol.sortedInsert([1, 3, 5], 0))  # expected: [0, 1, 3, 5]
    print(sol.sortedInsert([], 7))  # expected: [7]
    print(sol.sortedInsert([10, 20, 30], 25))  # expected: [10, 20, 25, 30]
