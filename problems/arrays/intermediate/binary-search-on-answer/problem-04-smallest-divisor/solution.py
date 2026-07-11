"""Find the Smallest Divisor Given a Threshold — LeetCode 1283.

Find the smallest positive divisor such that the sum of ceil(num / divisor)
over all elements is <= threshold. Solve with Binary Search on Answer over the
divisor range [1, max(nums)].
"""

from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """Return the smallest divisor whose ceil-division sum is <= threshold.

        Args:
            nums: The array of positive integers to divide.
            threshold: The maximum allowed value of the ceil-division sum.

        Returns:
            The smallest positive integer d such that
            sum(ceil(num / d) for num in nums) <= threshold.

        Example:
            >>> Solution().smallestDivisor([1, 2, 5, 9], 6)
            5
        """
        # TODO: implement using Binary Search on Answer over [1, max(nums)].
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestDivisor([1, 2, 5, 9], 6))                 # expected: 5
    print(sol.smallestDivisor([44, 22, 33, 11, 1], 5))          # expected: 44
    print(sol.smallestDivisor([21212, 10101, 12121], 1000000))  # expected: 1
