"""LeetCode 387 - First Unique Character in a String.

Return the index of the first non-repeating character, or -1 if there is none.
Fill in the body using a Character Frequency Count.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Return the index of the first character that appears exactly once.

        Args:
            s: A string of lowercase English letters.

        Returns:
            The smallest index i such that s[i] occurs exactly once in s, or -1 if
            every character repeats.

        Example:
            >>> Solution().firstUniqChar("leetcode")
            0
            >>> Solution().firstUniqChar("aabb")
            -1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))      # expected: 0
    print(sol.firstUniqChar("loveleetcode"))  # expected: 2
    print(sol.firstUniqChar("aabb"))          # expected: -1
