"""First Palindromic String — LeetCode 2108. Deque two-end check on each word."""
from collections import deque  # noqa: F401
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # TODO: for each word, deque it and compare popleft() vs pop(); return the
        # first palindrome, or "" if none
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))  # expected: 'ada'
    print(sol.firstPalindrome(["notapalindrome", "racecar"]))  # expected: 'racecar'
    print(sol.firstPalindrome(["def", "ghi"]))  # expected: ''
    print(sol.firstPalindrome(["z", "abc"]))  # expected: 'z'
    print(sol.firstPalindrome([]))  # expected: ''
