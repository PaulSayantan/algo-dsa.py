"""Single Number — LeetCode 136."""
from typing import List  # noqa: F401


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # TODO: every value appears twice except one; use a set to cancel pairs
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2, 2, 1]))  # expected: 1
    print(sol.singleNumber([4, 1, 2, 1, 2]))  # expected: 4
    print(sol.singleNumber([1]))  # expected: 1
    print(sol.singleNumber([7, 3, 5, 3, 7]))  # expected: 5
