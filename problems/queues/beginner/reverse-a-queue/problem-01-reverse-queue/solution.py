"""Reverse the order of a queue using a stack; return the reversed list."""
from typing import List  # noqa: F401


class Solution:
    def reverse(self, q: List[int]) -> List[int]:
        # TODO: dequeue all into a stack, then pop the stack back out (LIFO reverses FIFO)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse([1, 2, 3, 4, 5]))  # expected: [5, 4, 3, 2, 1]
    print(sol.reverse([7]))  # expected: [7]
    print(sol.reverse([]))  # expected: []
