"""Maximum Number of Non-overlapping Palindrome Substrings — LeetCode 2472.

Fill in the body using the expand-around-center technique combined with a
greedy left-to-right sweep.
"""


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        """Return the max count of non-overlapping palindromes of length >= k.

        Args:
            s: The input string (1 <= len(s) <= 2000), lowercase letters.
            k: Minimum required length of each selected palindrome (k >= 1).

        Returns:
            The maximum number of non-overlapping palindromic substrings of
            ``s`` that can be selected such that each has length at least ``k``.

        Example:
            >>> Solution().maxPalindromes("abaccdbbd", 3)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPalindromes("abaccdbbd", 3))  # expected: 2
    print(sol.maxPalindromes("adbcda", 2))     # expected: 0
    print(sol.maxPalindromes("aabbaa", 2))     # expected: 3
