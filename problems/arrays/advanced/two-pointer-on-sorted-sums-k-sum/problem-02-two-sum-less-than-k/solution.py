"""Two Sum Less Than K (LeetCode 1099).

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """Return the maximum pair sum strictly less than k, or -1 if none exists.

        Args:
            nums: List of positive integers (unsorted).
            k: Exclusive upper bound for the pair sum.

        Returns:
            The largest value ``nums[i] + nums[j]`` (with ``i < j``) that is
            strictly less than ``k``, or ``-1`` when no such pair exists.

        Example:
            >>> Solution().twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60)
            58
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60))  # expected: 58
    print(sol.twoSumLessThanK([10, 20, 30], 15))                    # expected: -1
    print(sol.twoSumLessThanK([1, 2, 3, 4], 5))                     # expected: 4
