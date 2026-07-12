"""All Nearest Smaller Values — both sides."""
from typing import List


class Solution:
    def nearestSmaller(self, nums: List[int]) -> List[List[int]]:
        # TODO: two monotonic-stack passes
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.nearestSmaller([4, 5, 2, 10, 8]))  # expected: [[-1, 2], [4, 2], [-1, -1], [2, 8], [2, -1]]
    print(sol.nearestSmaller([1, 2, 3]))  # expected: [[-1, -1], [1, -1], [2, -1]]
    print(sol.nearestSmaller([3, 2, 1]))  # expected: [[-1, 2], [-1, 1], [-1, -1]]
