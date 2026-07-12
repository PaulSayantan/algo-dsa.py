"""Missing Number — LeetCode 268."""
from typing import List  # noqa: F401


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # TODO: nums holds distinct values in [0, n]; find the one absent
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([3, 0, 1]))  # expected: 2
    print(sol.missingNumber([0, 1]))  # expected: 2
    print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # expected: 8
    print(sol.missingNumber([0]))  # expected: 1
