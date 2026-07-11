"""Shortest Palindrome (LeetCode 214).

Build the shortest palindrome by prepending characters, using a forward-vs-
reverse rolling hash to find the longest palindromic prefix in O(n).
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """Return the shortest palindrome formed by prepending chars to ``s``.

        Args:
            s: The input string (lowercase English letters, possibly empty).

        Returns:
            The shortest palindrome obtainable by adding characters only in front
            of ``s``.

        Example:
            >>> Solution().shortestPalindrome("aacecaaa")
            'aaacecaaa'
            >>> Solution().shortestPalindrome("abcd")
            'dcbabcd'
        """
        # TODO: implement with forward/reverse rolling hash.
        #   1. Scan i = 0..n-1 keeping fwd = hash(s[0..i]) and
        #      rev = hash(s[i..0]) (same chars reversed).
        #   2. The largest i+1 with fwd == rev is the longest palindromic prefix
        #      length k (verify to avoid collisions).
        #   3. Return s[k:][::-1] + s.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPalindrome("aacecaaa"))  # expected: "aaacecaaa"
    print(sol.shortestPalindrome("abcd"))       # expected: "dcbabcd"
    print(sol.shortestPalindrome("aba"))        # expected: "aba"
