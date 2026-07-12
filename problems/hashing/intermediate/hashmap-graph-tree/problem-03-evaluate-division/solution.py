"""Evaluate Division — LeetCode 399."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # TODO: weighted adjacency map; DFS multiplying edge ratios; -1.0 if unreachable
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))  # expected: [6.0, 0.5, -1.0, 1.0, -1.0]
