"""Is a permutation stack-sortable? (single-stack sort)."""
from typing import List


class Solution:
    def isStackSortable(self, perm: List[int]) -> bool:
        # TODO: simulate the stack sort; output must come out 1..n
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isStackSortable([2, 3, 1]))  # expected: False
    print(sol.isStackSortable([1, 2, 3]))  # expected: True
    print(sol.isStackSortable([3, 1, 2]))  # expected: True
    print(sol.isStackSortable([2, 4, 3, 1]))  # expected: False
