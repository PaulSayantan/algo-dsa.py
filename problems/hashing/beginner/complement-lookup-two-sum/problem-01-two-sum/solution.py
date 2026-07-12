"""Two Sum — LeetCode 1. Return indices of the two numbers adding to target."""
from typing import List  # noqa: F401


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TODO: store value -> index; for each x look up (target - x)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # expected: [0, 1]
    print(sol.twoSum([3, 2, 4], 6))  # expected: [1, 2]
    print(sol.twoSum([3, 3], 6))  # expected: [0, 1]
    print(sol.twoSum([1, 2, 3], 7))  # expected: []
