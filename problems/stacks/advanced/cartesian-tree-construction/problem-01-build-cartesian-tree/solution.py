"""Build a min-Cartesian tree; return the parent-index array."""
from typing import List


class Solution:
    def cartesianParents(self, nums: List[int]) -> List[int]:
        # TODO: monotonic increasing stack; track parents
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.cartesianParents([3, 2, 1, 5, 4]))  # expected: [1, 2, -1, 4, 2]
    print(sol.cartesianParents([1, 2, 3]))  # expected: [-1, 0, 1]
    print(sol.cartesianParents([9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]))  # expected: [1, 3, 1, -1, 10, 6, 4, 8, 6, 8, 3]
