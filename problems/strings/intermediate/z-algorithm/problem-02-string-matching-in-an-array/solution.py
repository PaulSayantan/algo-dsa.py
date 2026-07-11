"""LeetCode 1408 - String Matching in an Array.

For each word, decide whether it is a substring of some other word. Use the
Z-Algorithm on `candidate + separator + other` and check for a Z-value equal
to len(candidate).
"""

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """Return every word that is a substring of a different word.

        Args:
            words: A list of unique lowercase strings.

        Returns:
            A list containing each word in ``words`` that occurs as a contiguous
            substring of some other word. Order does not matter.

        Example:
            >>> sorted(Solution().stringMatching(["mass", "as", "hero", "superhero"]))
            ['as', 'hero']
            >>> Solution().stringMatching(["blue", "green", "bu"])
            []
        """
        # TODO: implement
        pass

    def _is_substring(self, pattern: str, text: str) -> bool:
        """Optional helper: True iff ``pattern`` occurs inside ``text``.

        Intended to use the Z-Algorithm on ``pattern + '#' + text``.

        Args:
            pattern: The candidate substring.
            text: The string to search within.

        Returns:
            Whether ``pattern`` is a contiguous substring of ``text``.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.stringMatching(["mass", "as", "hero", "superhero"]))  # expected: ["as", "hero"]
    print(sol.stringMatching(["leetcode", "et", "code"]))            # expected: ["et", "code"]
    print(sol.stringMatching(["blue", "green", "bu"]))               # expected: []
