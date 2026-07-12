"""Reverse a queue in consecutive groups of k using a stack per group."""
from typing import List  # noqa: F401


class Solution:
    def reverseInGroups(self, q: List[int], k: int) -> List[int]:
        # TODO: for each block of k, push onto a stack then pop it back to reverse that block
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseInGroups([1, 2, 3, 4, 5, 6, 7, 8], 3))  # expected: [3, 2, 1, 6, 5, 4, 8, 7]
    print(sol.reverseInGroups([1, 2, 3, 4, 5, 6], 3))  # expected: [3, 2, 1, 6, 5, 4]
    print(sol.reverseInGroups([1, 2, 3, 4], 2))  # expected: [2, 1, 4, 3]
    print(sol.reverseInGroups([1, 2, 3], 1))  # expected: [1, 2, 3]
