"""Two-Sum existence via a hash set — based on LeetCode 1 (Two Sum)."""
from typing import List  # noqa: F401


class Solution:
    def twoSumExists(self, nums: List[int], target: int) -> bool:
        # TODO: for each x, check whether target - x was already seen
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSumExists([2, 7, 11, 15], 9))  # expected: True
    print(sol.twoSumExists([3, 2, 4], 6))  # expected: True
    print(sol.twoSumExists([1, 2, 3], 7))  # expected: False
    print(sol.twoSumExists([3, 3], 6))  # expected: True
