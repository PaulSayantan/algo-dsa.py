"""Word Ladder — LeetCode 127 (BFS over hashed word states)."""
from typing import List  # noqa: F401


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # TODO: BFS changing one letter at a time through words in wordList;
        # visited set of words; return the shortest transformation length (or 0)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # expected: 5
    print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # expected: 0
    print(sol.ladderLength("a", "c", ["a", "b", "c"]))  # expected: 2
