"""Count Pairs Summing to Target. Count pairs i < j with nums[i] + nums[j] == target."""
from typing import List  # noqa: F401


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # TODO: for each x add how many earlier values equal (target - x)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countPairs([1, 2, 3, 4], 5))  # expected: 2
    print(sol.countPairs([1, 1, 1, 1], 2))  # expected: 6
    print(sol.countPairs([1, 2, 3], 7))  # expected: 0
    print(sol.countPairs([0, 0, 0], 0))  # expected: 3
    print(sol.countPairs([-1, 1, 2, -2, 3], 0))  # expected: 2
