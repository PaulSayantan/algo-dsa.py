"""Count Number of Pairs With Absolute Difference K — LeetCode 2006."""
from typing import List  # noqa: F401


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # TODO: for each x add how many earlier values equal x-k or x+k
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countKDifference([1, 2, 2, 1], 1))  # expected: 4
    print(sol.countKDifference([1, 3], 3))  # expected: 0
    print(sol.countKDifference([3, 2, 1, 5, 4], 2))  # expected: 3
    print(sol.countKDifference([2, 2, 2], 1))  # expected: 0
    print(sol.countKDifference([1, 2, 3, 4], 1))  # expected: 3
