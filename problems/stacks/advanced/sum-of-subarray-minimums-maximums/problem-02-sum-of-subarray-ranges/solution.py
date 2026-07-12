"""Sum of Subarray Ranges — LeetCode 2104."""
from typing import List


class Solution:
    def subarrayRanges(self, nums: List[int]) -> int:
        # TODO: sum of subarray maxima - sum of subarray minima
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarrayRanges([1, 2, 3]))  # expected: 4
    print(sol.subarrayRanges([1, 3, 3]))  # expected: 4
    print(sol.subarrayRanges([4, -2, -3, 4, 1]))  # expected: 59
