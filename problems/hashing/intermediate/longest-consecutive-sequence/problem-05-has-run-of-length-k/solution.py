"""Does a consecutive run of length >= k exist?"""
from typing import List  # noqa: F401


class Solution:
    def hasConsecutiveRun(self, nums: List[int], k: int) -> bool:
        # TODO: expand each run-start; return True once a run reaches length k
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.hasConsecutiveRun([1, 2, 3, 4], 3))  # expected: True
    print(sol.hasConsecutiveRun([1, 2, 3, 4], 5))  # expected: False
    print(sol.hasConsecutiveRun([10, 20, 30], 2))  # expected: False
    print(sol.hasConsecutiveRun([5, 6, 7, 1], 3))  # expected: True
    print(sol.hasConsecutiveRun([1, 2, 3], 0))  # expected: True
