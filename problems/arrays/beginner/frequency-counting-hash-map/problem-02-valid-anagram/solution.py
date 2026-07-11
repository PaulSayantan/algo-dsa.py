"""Valid Anagram (LeetCode 242).

Decide whether string ``t`` is an anagram of string ``s``.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Return True if ``t`` is an anagram of ``s``.

        Two strings are anagrams when they contain the same characters with the
        same frequencies, regardless of order.

        Args:
            s: The reference string.
            t: The candidate string to test against ``s``.

        Returns:
            True if ``t`` is a rearrangement of ``s``, otherwise False.

        Example:
            >>> Solution().isAnagram("anagram", "nagaram")
            True
            >>> Solution().isAnagram("rat", "car")
            False
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    solver = Solution()

    print(solver.isAnagram("anagram", "nagaram"))  # expected: True
    print(solver.isAnagram("rat", "car"))  # expected: False
    print(solver.isAnagram("ab", "a"))  # expected: False
