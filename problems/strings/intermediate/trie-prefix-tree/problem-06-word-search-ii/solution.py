"""LeetCode 212 - Word Search II.

Return every word from a list that can be traced on a grid of letters, using a Trie
to drive DFS backtracking.
"""
from __future__ import annotations

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """Find all words that appear on the board.

        A word is formed from sequentially adjacent (up/down/left/right) cells,
        with no cell reused within a single word. Each found word is returned
        once.

        Args:
            board: An m x n grid of lowercase letters.
            words: List of unique lowercase words to search for.

        Returns:
            A list of the words that can be traced on the board (any order).

        Example:
            >>> board = [["o","a","a","n"],
            ...          ["e","t","a","e"],
            ...          ["i","h","k","r"],
            ...          ["i","f","l","v"]]
            >>> sorted(Solution().findWords(board, ["oath","pea","eat","rain"]))
            ['eat', 'oath']
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    sol = Solution()
    print(sorted(sol.findWords(board, ["oath", "pea", "eat", "rain"])))
    # expected: ['eat', 'oath']
    print(sol.findWords([["a", "b"], ["c", "d"]], ["abcb"]))
    # expected: []
