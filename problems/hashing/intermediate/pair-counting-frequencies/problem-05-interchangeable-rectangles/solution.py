"""Number of Pairs of Interchangeable Rectangles — LeetCode 2001."""
from typing import List  # noqa: F401
from collections import Counter  # noqa: F401


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # TODO: group by reduced width:height ratio; add count[key] before incrementing
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.interchangeableRectangles([[4, 8], [3, 6], [10, 20], [15, 30]]))  # expected: 6
    print(sol.interchangeableRectangles([[4, 5], [7, 8]]))  # expected: 0
    print(sol.interchangeableRectangles([[1, 1], [2, 2], [3, 3]]))  # expected: 3
    print(sol.interchangeableRectangles([[6, 4], [3, 2], [9, 6]]))  # expected: 3
