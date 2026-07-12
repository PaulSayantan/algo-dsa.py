"""Cycle length reached from a start node in a functional graph."""
from typing import List


class Solution:
    def cycleLength(self, succ: List[int], start: int) -> int:
        # TODO: record each node's step; on revisit, cycle length = now - first-seen step
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.cycleLength([1, 2, 3, 4, 2], 0))  # expected: 3
    print(sol.cycleLength([1, 0], 0))  # expected: 2
    print(sol.cycleLength([0], 0))  # expected: 1
