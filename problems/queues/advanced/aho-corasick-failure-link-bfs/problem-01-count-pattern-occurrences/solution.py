"""Aho-Corasick: total occurrences of multiple patterns in a text."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def countOccurrences(self, patterns: List[str], text: str) -> int:
        # TODO: trie + BFS failure links + text scan
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countOccurrences(["he", "she", "his", "hers"], "ushers"))  # expected: 3
    print(sol.countOccurrences(["a", "ab", "abc"], "abcabc"))  # expected: 6
    print(sol.countOccurrences(["xyz"], "abcabc"))  # expected: 0
