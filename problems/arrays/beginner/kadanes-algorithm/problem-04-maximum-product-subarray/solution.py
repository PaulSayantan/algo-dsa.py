from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """Return the largest product of any contiguous non-empty subarray.

        Args:
            nums: A non-empty list of integers (may include negatives and zeros).

        Returns:
            The maximum product obtainable from any contiguous subarray.

        Example:
            >>> Solution().maxProduct([2, 3, -2, 4])
            6
        """
        # TODO: implement using a Kadane variant that tracks running max AND min
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4]))  # expected: 6
    print(sol.maxProduct([-2, 0, -1]))    # expected: 0
    print(sol.maxProduct([-2, 3, -4]))    # expected: 24
