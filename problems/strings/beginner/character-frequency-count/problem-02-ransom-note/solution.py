"""LeetCode 383 - Ransom Note.

Decide whether ransomNote can be built from the letters in magazine, where each
magazine letter may be used at most once. Fill in the body using a Character
Frequency Count.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """Return True if ransomNote can be assembled from magazine's letters.

        Args:
            ransomNote: The string we want to build (lowercase letters).
            magazine: The pool of available letters (lowercase letters), each
                usable at most once.

        Returns:
            True if magazine supplies at least as many of every character as
            ransomNote requires, otherwise False.

        Example:
            >>> Solution().canConstruct("aa", "aab")
            True
            >>> Solution().canConstruct("aa", "ab")
            False
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("a", "b"))     # expected: False
    print(sol.canConstruct("aa", "ab"))   # expected: False
    print(sol.canConstruct("aa", "aab"))  # expected: True
