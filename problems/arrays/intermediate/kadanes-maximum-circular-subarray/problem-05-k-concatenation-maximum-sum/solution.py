"""K-Concatenation Maximum Sum (LeetCode 1191).

Fill in the body of `kConcatenationMaxSum`. Do not modify the signature.
"""
from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        """Return the max subarray sum of ``arr`` repeated ``k`` times, mod 1e9+7.

        The subarray may be empty (sum 0), so the answer is always >= 0.

        Args:
            arr: The base integer array to be concatenated. Length >= 1.
            k: The number of times ``arr`` is concatenated with itself (>= 1).

        Returns:
            The maximum subarray sum of the length ``len(arr) * k`` array,
            taken modulo 10**9 + 7.

        Example:
            >>> Solution().kConcatenationMaxSum([1, 2], 3)
            9
        """
        # TODO: Let MOD = 10**9 + 7 and total = sum(arr).
        #   - If k == 1: return Kadane-with-empty-allowed over arr.
        #   - Else: let two = Kadane-with-empty-allowed over (arr + arr).
        #       if total > 0: answer = two + (k - 2) * total
        #       else:         answer = two
        #   Return answer % MOD (apply the modulo only at the end).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kConcatenationMaxSum([1, 2], 3))       # expected: 9
    print(sol.kConcatenationMaxSum([1, -2, 1], 5))   # expected: 2
    print(sol.kConcatenationMaxSum([-1, -2], 7))     # expected: 0
