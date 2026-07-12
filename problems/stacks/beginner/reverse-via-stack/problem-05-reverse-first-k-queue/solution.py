"""Reverse the first K elements of a queue using a stack."""
from typing import List


class Solution:
    def reverseFirstK(self, q: List[int], k: int) -> List[int]:
        # TODO: push the first k elements onto a stack, pop them to the front,
        # then append the remaining elements unchanged
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseFirstK([1, 2, 3, 4, 5], 3))  # expected: [3, 2, 1, 4, 5]
    print(sol.reverseFirstK([1, 2, 3, 4, 5], 5))  # expected: [5, 4, 3, 2, 1]
    print(sol.reverseFirstK([10, 20, 30], 1))  # expected: [10, 20, 30]
    print(sol.reverseFirstK([7, 8, 9], 0))  # expected: [7, 8, 9]
