"""Jump Game VI — LeetCode 1696.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """Return the maximum score to reach the last index.

        From index ``i`` you may jump to any ``j`` with ``i < j <= i + k``. The
        score is the sum of ``nums`` over every visited index, including index
        ``0`` and the final index ``len(nums) - 1``.

        Args:
            nums: The input array of integers (may contain negatives).
            k: The maximum forward jump length, with ``1 <= k <= len(nums)``.

        Returns:
            The maximum achievable score reaching index ``len(nums) - 1``.

        Example:
            >>> Solution().maxResult([1, -1, -2, 4, -7, 3], 2)
            7
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxResult([1, -1, -2, 4, -7, 3], 2))  # expected: 7
    print(sol.maxResult([10, -5, -2, 4, 0, 3], 3))  # expected: 17
    print(sol.maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2))  # expected: 0
