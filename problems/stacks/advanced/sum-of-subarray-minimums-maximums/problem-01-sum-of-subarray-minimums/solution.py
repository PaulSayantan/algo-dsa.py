"""Sum of Subarray Minimums — LeetCode 907."""
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # TODO: monotonic stack contribution counting, mod 1e9+7
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumSubarrayMins([3, 1, 2, 4]))  # expected: 17
    print(sol.sumSubarrayMins([11, 81, 94, 43, 3]))  # expected: 444
    print(sol.sumSubarrayMins([1]))  # expected: 1
