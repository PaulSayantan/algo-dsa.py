"""Sliding Puzzle — LeetCode 773 (bidirectional BFS)."""
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # TODO: BFS from both the start state and the solved goal; expand the smaller frontier
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.slidingPuzzle([[1, 2, 3], [4, 0, 5]]))  # expected: 1
    print(sol.slidingPuzzle([[1, 2, 3], [5, 4, 0]]))  # expected: -1
    print(sol.slidingPuzzle([[4, 1, 2], [5, 0, 3]]))  # expected: 5
    print(sol.slidingPuzzle([[1, 2, 3], [4, 5, 0]]))  # expected: 0
