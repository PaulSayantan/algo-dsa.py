"""Maximum Product Subarray (LeetCode 152) — divide & conquer template.

Each recursive call should summarize its range as a tuple:
    (total, max_prefix, min_prefix, max_suffix, min_suffix, best)
The merge combines two summaries in O(1): the best crossing product comes from
the four sign combinations of the left's max/min suffix and the right's max/min
prefix. Tracking the MIN is essential because negative * negative can become the
new maximum.
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """Return the largest product of any contiguous non-empty subarray.

        Args:
            nums: A non-empty list of integers (may include negatives and zeros).

        Returns:
            The maximum subarray product. Fits in a 32-bit signed integer.

        Example:
            >>> Solution().maxProduct([2, 3, -2, 4])
            6
        """
        # TODO: implement using Maximum Subarray via Divide & Conquer
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4]))  # expected: 6
    print(sol.maxProduct([-2, 0, -1]))    # expected: 0
    print(sol.maxProduct([-2, 3, -4]))    # expected: 24
