"""Sum of Subarray Minimums — LeetCode 907 (monotonic stack)."""
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # TODO: monotonic increasing stack; count left/right spans per element
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumSubarrayMins([3, 1, 2, 4]))  # expected: 17
    print(sol.sumSubarrayMins([11, 81, 94, 43, 3]))  # expected: 444
    print(sol.sumSubarrayMins([1]))  # expected: 1
    print(sol.sumSubarrayMins([2, 2]))  # expected: 6
