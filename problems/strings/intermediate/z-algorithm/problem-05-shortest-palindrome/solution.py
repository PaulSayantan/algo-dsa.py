"""LeetCode 214 - Shortest Palindrome.

Prepend the fewest characters to make s a palindrome. Find the longest
palindromic prefix of s using the Z-array of `s + separator + reverse(s)`, then
prepend the reverse of the leftover suffix.
"""

from typing import List


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """Return the shortest palindrome formable by prepending chars to s.

        Args:
            s: A lowercase string (possibly empty).

        Returns:
            The shortest palindrome that has ``s`` as a suffix, formed by adding
            characters only in front of ``s``.

        Example:
            >>> Solution().shortestPalindrome("aacecaaa")
            'aaacecaaa'
            >>> Solution().shortestPalindrome("abcd")
            'dcbabcd'
            >>> Solution().shortestPalindrome("")
            ''
        """
        # TODO: implement
        pass

    def _z_array(self, s: str) -> List[int]:
        """Optional helper: compute the Z-array of ``s`` in O(len(s)) time.

        Args:
            s: The string whose Z-array should be computed.

        Returns:
            A list ``z`` where ``z[i]`` is the length of the longest substring
            starting at ``i`` that is also a prefix of ``s``.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPalindrome("aacecaaa"))  # expected: "aaacecaaa"
    print(sol.shortestPalindrome("abcd"))       # expected: "dcbabcd"
    print(sol.shortestPalindrome("aabba"))      # expected: "abbaabba"
