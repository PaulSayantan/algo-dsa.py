"""LeetCode 480 - Sliding Window Median.

Solve with an Order-Statistics Tree: keep the current window as a dynamic
multiset supporting insert, delete, and select (k-th smallest) in O(log k).

This is an EMPTY TEMPLATE. Fill in the logic yourself.
"""
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """Return the median of every contiguous window of size k.

        Args:
            nums: The input integer array.
            k: The window size (1 <= k <= len(nums)).

        Returns:
            A list of floats: the median of each window, left to right. There are
            len(nums) - k + 1 windows.

        Example:
            Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
            # -> [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
        """
        # TODO: implement
        # - insert first k elements into the OST
        # - for each window: read median via select (one select if k is odd,
        #   average of two selects if k is even), then delete the outgoing
        #   element and insert the incoming one
        pass


if __name__ == "__main__":
    print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # expected [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    print(Solution().medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3))
    # expected [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
