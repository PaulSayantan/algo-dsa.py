"""Find All Anagrams in a String — LeetCode 438.

Return the start indices of every window in ``s`` that is an anagram of ``p``,
by sliding a fixed-width window and comparing count signatures.
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """Return all start indices of anagrams of ``p`` within ``s``.

        Args:
            s: The text to search, lowercase English letters.
            p: The pattern whose anagrams we look for, lowercase English letters.

        Returns:
            A list of 0-based start indices ``i`` such that ``s[i:i+len(p)]`` is
            an anagram of ``p``. Order does not matter.

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
    print(sol.findAnagrams("abab", "ab"))          # expected: [0, 1, 2]
    print(sol.findAnagrams("aa", "bb"))            # expected: []
