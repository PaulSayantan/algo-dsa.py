from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Return the largest sum of any contiguous non-empty subarray.

        Args:
            nums: A non-empty list of integers (may include negatives).

        Returns:
            The maximum sum obtainable from any contiguous subarray of ``nums``.

        Example:
            >>> Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
            6
        """
        maxSum = nums[0]
        subarraySum = nums[0]
        for i in range(1, len(nums)):
            subarraySum = max(nums[i], subarraySum+nums[i])
            maxSum = max(maxSum, subarraySum)
        return maxSum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected: 6
    #print(sol.maxSubArray([1]))                               # expected: 1
    #print(sol.maxSubArray([5, 4, -1, 7, 8]))                  # expected: 23
