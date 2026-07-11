"""Maximum Average Subarray I (LeetCode 643).

Fill in the body using the Sliding Window technique.
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """Return the maximum average of any contiguous subarray of length k.

        Args:
            nums: The list of integers to scan.
            k: The exact length of the subarray whose average is maximized.

        Returns:
            The maximum average value as a float. An answer within 1e-5 of the
            true maximum is acceptable.

        Example:
            >>> Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4)
            12.75
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # expected: 12.75
    print(sol.findMaxAverage([5], 1))                       # expected: 5.0
    print(sol.findMaxAverage([0, 4, 0, 3, 2], 1))           # expected: 4.0
