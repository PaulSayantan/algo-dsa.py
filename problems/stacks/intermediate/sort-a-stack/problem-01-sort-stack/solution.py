"""Sort a stack using one auxiliary stack."""
from typing import List


class Solution:
    def sortStack(self, stack: List[int]) -> List[int]:
        # TODO: use one temp stack; insertion-sort style
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortStack([34, 3, 31, 98, 92, 23]))  # expected: [3, 23, 31, 34, 92, 98]
    print(sol.sortStack([3, 1, 2]))  # expected: [1, 2, 3]
    print(sol.sortStack([]))  # expected: []
    print(sol.sortStack([5]))  # expected: [5]
