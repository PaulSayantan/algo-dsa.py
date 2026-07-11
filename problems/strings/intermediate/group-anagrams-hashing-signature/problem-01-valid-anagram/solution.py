"""Valid Anagram — LeetCode 242.

Determine whether two strings are anagrams of each other by comparing their
character-count signatures.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Return True if ``t`` is an anagram of ``s``.

        Args:
            s: The first string of lowercase English letters.
            t: The second string of lowercase English letters.

        Returns:
            True if ``s`` and ``t`` contain exactly the same characters with the
            same frequencies (i.e. they are anagrams), otherwise False.

        Example:
            >>> Solution().isAnagram("anagram", "nagaram")
            True
            >>> Solution().isAnagram("rat", "car")
            False
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # expected: True
    print(sol.isAnagram("rat", "car"))          # expected: False
    print(sol.isAnagram("a", "ab"))             # expected: False
