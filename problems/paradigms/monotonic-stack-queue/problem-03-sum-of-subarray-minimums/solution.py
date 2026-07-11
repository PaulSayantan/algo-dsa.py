"""Sum of Subarray Minimums — LeetCode 907.

Fill in the body of `sumSubarrayMins`. Do not modify the signature.
"""
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """Return the sum of the minimum of every contiguous subarray, mod 1e9+7.

        Args:
            arr: A list of positive integers.

        Returns:
            The sum over all subarrays `b` of `min(b)`, taken modulo 10**9 + 7.

        Example:
            >>> Solution().sumSubarrayMins([3, 1, 2, 4])
            17
        """
        # TODO: implement with a monotonic stack. For each index i, compute the
        # number of subarrays in which arr[i] is the minimum using distances to
        # the previous strictly-smaller and next smaller-or-equal elements, then
        # accumulate arr[i] * left * right (mod 1e9+7).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumSubarrayMins([3, 1, 2, 4]))          # expected: 17
    print(sol.sumSubarrayMins([11, 81, 94, 43, 3]))   # expected: 444
