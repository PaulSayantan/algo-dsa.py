"""Sliding Puzzle — LeetCode 773 (BFS over hashed board states)."""
from typing import List  # noqa: F401


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # TODO: BFS from the serialized start board to "123450"; keep visited
        # states in a set of strings; return the minimum number of moves (or -1)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.slidingPuzzle([[1, 2, 3], [4, 0, 5]]))  # expected: 1
    print(sol.slidingPuzzle([[1, 2, 3], [5, 4, 0]]))  # expected: -1
    print(sol.slidingPuzzle([[4, 1, 2], [5, 0, 3]]))  # expected: 5
