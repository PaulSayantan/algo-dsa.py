from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """Return the maximum non-empty subarray sum of a circular array.

        Args:
            nums: A non-empty list of integers viewed as a circular buffer,
                where the element after ``nums[-1]`` is ``nums[0]``.

        Returns:
            The maximum sum of any non-empty subarray, allowing wrap-around.

        Example:
            >>> Solution().maxSubarraySumCircular([5, -3, 5])
            10
        """
        # TODO: implement with two Kadane passes (max subarray and min subarray)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubarraySumCircular([1, -2, 3, -2]))  # expected: 3
    print(sol.maxSubarraySumCircular([5, -3, 5]))      # expected: 10
    print(sol.maxSubarraySumCircular([-3, -2, -3]))    # expected: -2
