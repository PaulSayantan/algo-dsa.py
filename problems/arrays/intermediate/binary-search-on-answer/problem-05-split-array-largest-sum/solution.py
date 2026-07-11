"""Split Array Largest Sum — LeetCode 410.

Split nums into k non-empty contiguous subarrays so that the largest subarray
sum is minimized, and return that minimized largest sum. Solve with Binary
Search on Answer over the range [max(nums), sum(nums)].
"""

from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """Return the minimized largest subarray sum over all k-way splits.

        Args:
            nums: The array of non-negative integers to split.
            k: The number of contiguous, non-empty subarrays to split into.

        Returns:
            The smallest possible value of the maximum subarray sum when nums is
            partitioned into exactly k contiguous subarrays.

        Example:
            >>> Solution().splitArray([7, 2, 5, 10, 8], 2)
            18
        """
        # TODO: implement using Binary Search on Answer over
        #       [max(nums), sum(nums)].
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.splitArray([7, 2, 5, 10, 8], 2))  # expected: 18
    print(sol.splitArray([1, 2, 3, 4, 5], 2))   # expected: 9
    print(sol.splitArray([1, 4, 4], 3))         # expected: 4
