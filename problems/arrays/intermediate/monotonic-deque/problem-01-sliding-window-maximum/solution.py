"""Sliding Window Maximum — LeetCode 239.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Return the maximum of every contiguous window of size ``k``.

        Args:
            nums: The input array of integers.
            k: The (fixed) window size, with ``1 <= k <= len(nums)``.

        Returns:
            A list of length ``len(nums) - k + 1`` whose ``i``-th entry is the
            maximum of ``nums[i:i + k]``.

        Example:
            >>> Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
            [3, 3, 5, 5, 6, 7]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # expected: [3, 3, 5, 5, 6, 7]
    print(sol.maxSlidingWindow([1], 1))  # expected: [1]
    print(sol.maxSlidingWindow([9, 10, 9, -7, -4, -8, 2, -6], 5))
    # expected: [10, 10, 9, 2]
