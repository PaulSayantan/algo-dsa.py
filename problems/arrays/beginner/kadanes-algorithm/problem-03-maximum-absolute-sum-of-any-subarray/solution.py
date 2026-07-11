from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """Return the maximum absolute sum of any (possibly empty) subarray.

        Args:
            nums: A non-empty list of integers (may include negatives).

        Returns:
            The largest value of ``abs(sum(subarray))`` over all subarrays.

        Example:
            >>> Solution().maxAbsoluteSum([1, -3, 2, 3, -4])
            5
        """
        # TODO: implement by running Kadane's Algorithm for both max and min sums
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAbsoluteSum([1, -3, 2, 3, -4]))       # expected: 5
    print(sol.maxAbsoluteSum([2, -5, 1, -4, 3, -2]))   # expected: 8
