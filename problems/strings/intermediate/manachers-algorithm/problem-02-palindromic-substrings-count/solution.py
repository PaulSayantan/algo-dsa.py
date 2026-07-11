"""Palindromic Substrings (LeetCode 647).

Fill in the body of `countSubstrings` using Manacher's Algorithm.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """Count the number of palindromic substrings in ``s``.

        Substrings starting or ending at different indices are counted
        separately even if their contents are identical.

        Args:
            s: The input string (lowercase English letters).

        Returns:
            The total number of palindromic substrings.

        Example:
            >>> Solution().countSubstrings("aaa")
            6
        """
        # TODO: implement using Manacher's Algorithm
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings("abc"))   # expected: 3
    print(sol.countSubstrings("aaa"))   # expected: 6
    print(sol.countSubstrings("abba"))  # expected: 6
