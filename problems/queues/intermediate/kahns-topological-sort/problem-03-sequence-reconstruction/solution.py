"""Sequence Reconstruction — LeetCode 444."""
from typing import List
from collections import deque, defaultdict  # noqa: F401


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # TODO: Kahn's algorithm; unique iff the queue never holds >1 node and order == nums
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3]]))  # expected: False
    print(sol.sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3], [2, 3]]))  # expected: True
    print(sol.sequenceReconstruction([1, 2, 3], [[1, 2]]))  # expected: False
    print(sol.sequenceReconstruction([1], [[1]]))  # expected: True
