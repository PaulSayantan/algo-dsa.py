"""Sort a stack in descending order using one auxiliary stack."""
from typing import List


class Solution:
    def sortStackDesc(self, stack: List[int]) -> List[int]:
        # TODO: one temp stack; before pushing cur, move temp's smaller elements back
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortStackDesc([34, 3, 31, 98, 92, 23]))  # expected: [98, 92, 34, 31, 23, 3]
    print(sol.sortStackDesc([3, 1, 2]))  # expected: [3, 2, 1]
    print(sol.sortStackDesc([]))  # expected: []
    print(sol.sortStackDesc([5]))  # expected: [5]
    print(sol.sortStackDesc([7, 7, 3]))  # expected: [7, 7, 3]
