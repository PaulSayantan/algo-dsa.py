"""Find and Replace Pattern — LeetCode 890.

Return every word that matches ``pattern`` under a bijective letter mapping, by
comparing canonical isomorphism (first-occurrence) signatures.
"""

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """Return the words in ``words`` that match ``pattern``.

        A word matches ``pattern`` when there is a bijection between letters that
        transforms ``pattern`` into the word.

        Args:
            words: A list of candidate words, all the same length as ``pattern``.
            pattern: The pattern string of lowercase English letters.

        Returns:
            The subset of ``words`` (in any order) that match ``pattern``.

        Example:
            >>> Solution().findAndReplacePattern(
            ...     ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb")
            ['mee', 'aqq']
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAndReplacePattern(
        ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
    # expected: ["mee", "aqq"]
    print(sol.findAndReplacePattern(["a", "b", "c"], "a"))
    # expected: ["a", "b", "c"]
    print(sol.findAndReplacePattern(["xyx", "yxy", "xxx"], "aba"))
    # expected: ["xyx", "yxy"]
