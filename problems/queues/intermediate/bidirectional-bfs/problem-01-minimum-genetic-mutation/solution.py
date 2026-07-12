"""Minimum Genetic Mutation — LeetCode 433 (bidirectional BFS)."""
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # TODO: bidirectional BFS meeting in the middle
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # expected: 1
    print(sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))  # expected: 2
    print(sol.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]))  # expected: 3
