"""Jump Game III — LeetCode 1306."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # TODO: BFS from start over i+arr[i] / i-arr[i]; success when arr[i] == 0
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.canReach([4, 2, 3, 0, 3, 1, 2], 5))  # expected: True
    print(sol.canReach([4, 2, 3, 0, 3, 1, 2], 0))  # expected: True
    print(sol.canReach([3, 0, 2, 1, 2], 2))  # expected: False
