"""Minimum Jumps to Reach Home — LeetCode 1654."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # TODO: BFS over (position, came_by_backward) states from (0, False);
        # forward +a always allowed, backward -b only if last jump was forward
        ...


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumJumps([14, 4, 18, 1, 15], 3, 15, 9))  # expected: 3
    print(sol.minimumJumps([8, 3, 16, 6, 12, 20], 15, 13, 11))  # expected: -1
    print(sol.minimumJumps([1, 6, 2, 14, 5, 17, 4], 16, 9, 7))  # expected: 2
    print(sol.minimumJumps([], 3, 2, 8))  # expected: 6
