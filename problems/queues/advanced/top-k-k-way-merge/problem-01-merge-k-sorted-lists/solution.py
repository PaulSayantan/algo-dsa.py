"""Merge k Sorted Lists — LeetCode 23 (list form)."""
from typing import List
import heapq  # noqa: F401


class Solution:
    def mergeKLists(self, lists: List[List[int]]) -> List[int]:
        # TODO: min-heap of (value, list_idx, elem_idx)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]]))  # expected: [1, 1, 2, 3, 4, 4, 5, 6]
    print(sol.mergeKLists([]))  # expected: []
    print(sol.mergeKLists([[], [1]]))  # expected: [1]
