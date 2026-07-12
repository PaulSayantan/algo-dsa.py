"""Equal Row and Column Pairs — LeetCode 2352."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # TODO: hash each row tuple; for each column tuple add the matching row count
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))  # expected: 1
    print(sol.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))  # expected: 3
    print(sol.equalPairs([[1, 1], [1, 1]]))  # expected: 4
