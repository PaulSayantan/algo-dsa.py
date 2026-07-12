"""Josephus k-th eliminated: return the m-th person removed via circular-queue simulation."""
from collections import deque  # noqa: F401


class Solution:
    def kthEliminated(self, n: int, k: int, m: int) -> int:
        # TODO: seat 1..n in a queue; rotate k-1 people to the back and remove the
        # k-th, recording each removed person; return the m-th one removed
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kthEliminated(7, 3, 1))  # expected: 3
    print(sol.kthEliminated(7, 3, 6))  # expected: 1
    print(sol.kthEliminated(5, 2, 3))  # expected: 1
    print(sol.kthEliminated(6, 3, 2))  # expected: 6
