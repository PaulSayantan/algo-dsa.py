"""Maximum Product of the Length of Two Palindromic Substrings (LeetCode 1960).

Fill in the body of `maxProduct`. Use the odd-length variant of Manacher's
Algorithm plus prefix/suffix sweeps over palindrome lengths.
"""


class Solution:
    def maxProduct(self, s: str) -> int:
        """Maximum product of lengths of two non-overlapping odd palindromes.

        Args:
            s: A 0-indexed string of odd length (lowercase English letters).

        Returns:
            The maximum product ``len(A) * len(B)`` over two non-intersecting
            odd-length palindromic substrings A and B.

        Example:
            >>> Solution().maxProduct("ababbb")
            9
        """
        # TODO: implement using Manacher's Algorithm + prefix/suffix sweeps
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct("ababbb"))     # expected: 9
    print(sol.maxProduct("zaaaxbbby"))  # expected: 9
    print(sol.maxProduct("aba"))        # expected: 1
