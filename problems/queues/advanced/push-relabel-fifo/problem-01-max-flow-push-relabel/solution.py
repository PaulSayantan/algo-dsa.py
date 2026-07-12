"""Maximum flow via FIFO push-relabel."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def maxFlow(self, n: int, edges: List[List[int]], s: int, t: int) -> int:
        # TODO: preflow + heights + queue of active nodes
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxFlow(4, [[0, 1, 3], [0, 2, 2], [1, 2, 1], [1, 3, 2], [2, 3, 3]], 0, 3))  # expected: 5
    print(sol.maxFlow(6, [[0, 1, 16], [0, 2, 13], [1, 2, 10], [2, 1, 4], [1, 3, 12], [3, 2, 9], [2, 4, 14], [4, 3, 7], [3, 5, 20], [4, 5, 4]], 0, 5))  # expected: 23
    print(sol.maxFlow(2, [[0, 1, 9]], 0, 1))  # expected: 9
