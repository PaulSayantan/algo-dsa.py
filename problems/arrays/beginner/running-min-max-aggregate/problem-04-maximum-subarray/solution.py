from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Return the largest sum of any contiguous non-empty subarray.

        Args:
            nums: A non-empty list of integers (may include negatives).

        Returns:
            The maximum subarray sum. For an all-negative array this is the
            single largest element.

        Example:
            >>> Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
            6
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected: 6
    print(sol.maxSubArray([1]))                              # expected: 1
    print(sol.maxSubArray([-3, -1, -2]))                     # expected: -1
