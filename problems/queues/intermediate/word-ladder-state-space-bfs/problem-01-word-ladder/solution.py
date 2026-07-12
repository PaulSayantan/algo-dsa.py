"""Word Ladder — LeetCode 127."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # TODO: state-space BFS over one-letter changes
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # expected: 5
    print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # expected: 0
    print(sol.ladderLength("a", "c", ["a", "b", "c"]))  # expected: 2
