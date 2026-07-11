from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        """Return the max subarray sum of ``arr`` repeated ``k`` times, mod 1e9+7.

        Args:
            arr: The base integer array to be repeated.
            k: The number of times ``arr`` is concatenated (>= 1).

        Returns:
            The maximum subarray sum (empty subarray allowed, so >= 0) of the
            k-times-repeated array, taken modulo 10**9 + 7.

        Example:
            >>> Solution().kConcatenationMaxSum([1, 2], 3)
            9
        """
        # TODO: implement using Kadane on one/two copies plus (k-2)*sum when sum>0
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kConcatenationMaxSum([1, 2], 3))       # expected: 9
    print(sol.kConcatenationMaxSum([1, -2, 1], 5))   # expected: 2
    print(sol.kConcatenationMaxSum([-1, -2], 7))     # expected: 0
