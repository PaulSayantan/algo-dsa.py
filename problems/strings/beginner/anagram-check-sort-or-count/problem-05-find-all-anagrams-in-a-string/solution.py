"""LeetCode 438 - Find All Anagrams in a String.

Fill in the body of `findAnagrams`. Do not change the signature.
"""

from collections import Counter  # noqa: F401  (available if you choose to use it)
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """Return all start indices where an anagram of `p` begins in `s`.

        Args:
            s: The text to search (lowercase English letters).
            p: The pattern whose anagrams we look for.

        Returns:
            A list of every index i such that s[i : i + len(p)] is an anagram of p.
            The indices may be returned in any order.

        Example:
            >>> Solution().findAnagrams("cbaebabacd", "abc")
            [0, 6]
            >>> Solution().findAnagrams("abab", "ab")
            [0, 1, 2]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd", "abc"))  # expected: [0, 6]
    print(sol.findAnagrams("abab", "ab"))         # expected: [0, 1, 2]
    print(sol.findAnagrams("aa", "bb"))           # expected: []
