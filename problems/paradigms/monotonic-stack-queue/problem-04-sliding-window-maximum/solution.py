"""Sliding Window Maximum — LeetCode 239.

Fill in the body of `maxSlidingWindow`. Do not modify the signature.
"""
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Return the maximum of every contiguous window of size k.

        Args:
            nums: A list of integers.
            k: The window size (1 <= k <= len(nums)).

        Returns:
            A list of length len(nums) - k + 1 where the i-th entry is the maximum
            of nums[i : i + k].

        Example:
            >>> Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
            [3, 3, 5, 5, 6, 7]
        """
        # TODO: implement using a monotonic deque of indices (decreasing values).
        # Pop smaller values from the back before appending i; pop the front when
        # it falls out of the window; record nums[front] once the first window forms.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # expected: [3, 3, 5, 5, 6, 7]
    print(sol.maxSlidingWindow([1], 1))
    # expected: [1]
