"""LeetCode 242 - Valid Anagram.

Determine whether two strings contain the same characters with the same counts.
Fill in the body using a Character Frequency Count.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Return True if t is an anagram of s.

        Args:
            s: The first lowercase string.
            t: The candidate anagram (also lowercase).

        Returns:
            True if t is a rearrangement of s using all the same letters with the
            same multiplicities, otherwise False.

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
