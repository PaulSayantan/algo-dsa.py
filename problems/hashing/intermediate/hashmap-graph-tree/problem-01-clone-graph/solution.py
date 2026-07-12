"""Clone Graph — LeetCode 133 (return a deterministic summary of the clone)."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def cloneGraphSummary(self, n: int, edges: List[List[int]]) -> list:
        # TODO: clone via an original->copy map; return [node_count, sorted clone edges]
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.cloneGraphSummary(4, [[1, 2], [1, 4], [2, 3], [3, 4]]))  # expected: [4, [(1, 2), (1, 4), (2, 3), (3, 4)]]
    print(sol.cloneGraphSummary(1, []))  # expected: [1, []]
    print(sol.cloneGraphSummary(3, [[1, 2]]))  # expected: [3, [(1, 2)]]
