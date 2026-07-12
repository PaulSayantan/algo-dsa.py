"""Minimum Knight Moves — LeetCode 1197 (bidirectional BFS)."""


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # TODO: fold to first quadrant, then two-frontier BFS from (0,0) and target
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minKnightMoves(2, 1))  # expected: 1
    print(sol.minKnightMoves(5, 5))  # expected: 4
    print(sol.minKnightMoves(0, 0))  # expected: 0
    print(sol.minKnightMoves(1, 1))  # expected: 2
    print(sol.minKnightMoves(4, 4))  # expected: 4
