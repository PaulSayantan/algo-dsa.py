"""Check whether a queue is a palindrome by reversing it with a stack."""
from typing import List  # noqa: F401


class Solution:
    def isPalindrome(self, q: List[int]) -> bool:
        # TODO: push all onto a stack to build the reversed queue, then compare with the original
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome([1, 2, 3, 2, 1]))  # expected: True
    print(sol.isPalindrome([1, 2, 3, 4]))  # expected: False
    print(sol.isPalindrome([7]))  # expected: True
    print(sol.isPalindrome([]))  # expected: True
