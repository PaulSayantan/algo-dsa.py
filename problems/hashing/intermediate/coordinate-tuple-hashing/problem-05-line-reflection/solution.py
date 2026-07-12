"""Line Reflection — LeetCode 356."""
from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # TODO: mirror line x=(min+max)/2; every point needs its reflection in the set
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isReflected([[1, 1], [-1, 1]]))  # expected: True
    print(sol.isReflected([[1, 1], [-1, -1]]))  # expected: False
    print(sol.isReflected([[0, 0], [2, 0], [1, 1], [1, -1]]))  # expected: True
