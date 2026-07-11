"""LeetCode 648 - Replace Words.

Replace each word in a sentence by the shortest dictionary root that is a prefix of it.
"""
from __future__ import annotations

from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """Replace successors in ``sentence`` with their shortest matching root.

        Args:
            dictionary: List of root words (lowercase letters).
            sentence: Space-separated lowercase words.

        Returns:
            The sentence with every word replaced by the shortest dictionary
            root that prefixes it; words with no matching root are unchanged.

        Example:
            >>> Solution().replaceWords(["cat", "bat", "rat"],
            ...                         "the cattle was rattled by the battery")
            'the cat was rat by the bat'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.replaceWords(["cat", "bat", "rat"],
                           "the cattle was rattled by the battery"))
    # expected: "the cat was rat by the bat"
    print(sol.replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"))
    # expected: "a a b c"
