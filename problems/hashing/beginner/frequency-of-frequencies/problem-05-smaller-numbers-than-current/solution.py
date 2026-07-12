"""How Many Numbers Are Smaller Than the Current Number — LeetCode 1365."""
from typing import List  # noqa: F401


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # TODO: bucket the counts (values are 0..100), then prefix-sum them
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  # expected: [4, 0, 1, 1, 3]
    print(sol.smallerNumbersThanCurrent([6, 5, 4, 8]))  # expected: [2, 1, 0, 3]
    print(sol.smallerNumbersThanCurrent([7, 7, 7, 7]))  # expected: [0, 0, 0, 0]
