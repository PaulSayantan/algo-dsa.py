"""First Unique Character in a String (LeetCode 387).

Return the index of the first non-repeating character, or -1 if none exists.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Return the index of the first character in ``s`` that appears once.

        Args:
            s: A string of lowercase English letters.

        Returns:
            The index of the earliest character with frequency one, or -1 if
            every character repeats.

        Example:
            >>> Solution().firstUniqChar("leetcode")
            0
            >>> Solution().firstUniqChar("loveleetcode")
            2
            >>> Solution().firstUniqChar("aabb")
            -1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    solver = Solution()

    print(solver.firstUniqChar("leetcode"))  # expected: 0
    print(solver.firstUniqChar("loveleetcode"))  # expected: 2
    print(solver.firstUniqChar("aabb"))  # expected: -1
