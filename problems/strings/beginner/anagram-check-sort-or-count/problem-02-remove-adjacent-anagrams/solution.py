"""Remove Adjacent Anagrams.

Collapse each run of adjacent anagrams to its first word.
Fill in the body of `removeAnagrams`. Do not change the signature.
"""

from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """Delete every word that is an anagram of its surviving predecessor.

        Args:
            words: A list of lowercase words.

        Returns:
            The list after repeatedly removing any word that is an anagram of
            the word immediately preceding it, until no such pair remains.

        Example:
            >>> Solution().removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"])
            ['abba', 'cd']
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"]))  # expected: ['abba', 'cd']
    print(sol.removeAnagrams(["a", "b", "a"]))                       # expected: ['a', 'b', 'a']
    print(sol.removeAnagrams(["hello", "olleh", "world"]))           # expected: ['hello', 'world']
