"""Number of Boomerangs — LeetCode 447."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        # TODO: per anchor, hash squared distances; add c*(c-1) per group
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))  # expected: 2
    print(sol.numberOfBoomerangs([[1, 1], [2, 2], [3, 3]]))  # expected: 2
    print(sol.numberOfBoomerangs([[0, 0]]))  # expected: 0
