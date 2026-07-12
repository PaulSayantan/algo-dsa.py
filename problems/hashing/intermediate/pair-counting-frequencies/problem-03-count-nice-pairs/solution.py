"""Count Nice Pairs in an Array — LeetCode 1814."""
from typing import List  # noqa: F401
from collections import Counter  # noqa: F401


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # TODO: group by (num - reverse(num)); sum f*(f-1)//2 over groups, mod 1e9+7
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countNicePairs([42, 11, 1, 97]))  # expected: 2
    print(sol.countNicePairs([13, 10, 35, 24, 76]))  # expected: 4
    print(sol.countNicePairs([1, 2, 3]))  # expected: 3
    print(sol.countNicePairs([100, 200, 300]))  # expected: 0
