"""Valid Palindrome — LeetCode 125. Alphanumeric-only, case-insensitive, via a deque."""
from collections import deque  # noqa: F401


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TODO: keep only alphanumerics (lowercased) in a deque, then two-end compare
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # expected: True
    print(sol.isPalindrome("race a car"))  # expected: False
    print(sol.isPalindrome(" "))  # expected: True
    print(sol.isPalindrome("0P"))  # expected: False
    print(sol.isPalindrome("ab_a"))  # expected: True
