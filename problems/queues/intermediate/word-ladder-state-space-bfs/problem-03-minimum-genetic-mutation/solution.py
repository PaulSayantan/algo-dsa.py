"""Minimum Genetic Mutation — LeetCode 433."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # TODO: state-space BFS; a neighbor flips one base and must be in the bank
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # expected: 1
    print(sol.minMutation(
        "AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    ))  # expected: 2
    print(sol.minMutation(
        "AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    ))  # expected: 3
    print(sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGCTA"]))  # expected: -1
