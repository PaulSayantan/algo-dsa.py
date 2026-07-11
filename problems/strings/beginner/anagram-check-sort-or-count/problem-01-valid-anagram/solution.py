"""LeetCode 242 - Valid Anagram.

Fill in the body of `isAnagram`. Do not change the signature.
"""

from collections import Counter  # noqa: F401  (available if you choose to use it)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Return True if `t` is an anagram of `s`, else False.

        Args:
            s: The reference string (lowercase English letters).
            t: The candidate string to test as a rearrangement of `s`.

        Returns:
            True if and only if `t` uses exactly the same characters as `s`
            with the same frequencies (implying equal lengths).

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
