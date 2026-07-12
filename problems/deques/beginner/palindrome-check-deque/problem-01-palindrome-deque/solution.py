"""Palindrome check with a deque: compare popFront vs popBack until <=1 left."""
from collections import deque  # noqa: F401
from typing import Union, List  # noqa: F401


class Solution:
    def isPalindrome(self, s: Union[str, List]) -> bool:
        # TODO: load into a deque; compare popleft() vs pop() each step
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("racecar"))  # expected: True
    print(sol.isPalindrome("abba"))  # expected: True
    print(sol.isPalindrome("abc"))  # expected: False
    print(sol.isPalindrome(""))  # expected: True
    print(sol.isPalindrome("x"))  # expected: True
    print(sol.isPalindrome([1, 2, 1]))  # expected: True
    print(sol.isPalindrome([1, 2, 3]))  # expected: False
