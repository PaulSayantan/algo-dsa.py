"""Word Search II (LeetCode 212).

Empty solution template — fill in the Trie-driven backtracking yourself.
"""
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """Return every word from `words` that can be traced through adjacent
        board cells (up/down/left/right), with no cell reused within a word.

        Args:
            board: An m x n grid of single lowercase-letter strings.
            words: The list of candidate words to search for.

        Returns:
            A list of the words that appear on the board, each at most once,
            in any order.

        Example:
            >>> sorted(Solution().findWords(
            ...     [["o", "a", "a", "n"],
            ...      ["e", "t", "a", "e"],
            ...      ["i", "h", "k", "r"],
            ...      ["i", "f", "l", "v"]],
            ...     ["oath", "pea", "eat", "rain"],
            ... ))
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
    print(Solution().findWords(board, ["oath", "pea", "eat", "rain"]))
    # Expected (any order): ["eat", "oath"]
    print(Solution().findWords([["a", "b"], ["c", "d"]], ["abcb"]))  # Expected: []
    print(Solution().findWords([["a"]], ["a", "aa"]))                # Expected: ["a"]
