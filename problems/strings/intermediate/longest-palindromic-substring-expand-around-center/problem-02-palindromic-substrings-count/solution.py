"""Palindromic Substrings — LeetCode 647.

Fill in the body using the expand-around-center technique.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """Count the palindromic substrings of ``s`` (counted by position).

        Args:
            s: The input string (1 <= len(s) <= 1000), lowercase letters.

        Returns:
            The number of contiguous substrings of ``s`` that are palindromes,
            where substrings at different index ranges are counted separately.

        Example:
            >>> Solution().countSubstrings("aaa")
            6
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings("abc"))  # expected: 3
    print(sol.countSubstrings("aaa"))  # expected: 6
    print(sol.countSubstrings("aba"))  # expected: 4
