"""Palindrome Number — LeetCode 9. Reject negatives, then deque two-end digit compare."""
from collections import deque  # noqa: F401


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # TODO: negatives are never palindromes; else load str(x) digits into a
        # deque and compare popleft() vs pop()
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))    # expected: True
    print(sol.isPalindrome(-121))   # expected: False
    print(sol.isPalindrome(10))     # expected: False
    print(sol.isPalindrome(0))      # expected: True
    print(sol.isPalindrome(12321))  # expected: True
