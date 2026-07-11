"""Count of Smaller Numbers After Self (LeetCode 315).

Fill in `Solution.countSmaller` using the merge-sort inversion-counting
technique, attributing each inversion to its left endpoint.
"""
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """For each index i, count elements to the right of i smaller than nums[i].

        Args:
            nums: A list of integers, length 1 <= n <= 10^5.

        Returns:
            A list `counts` of the same length where counts[i] is the number of
            j > i with nums[j] < nums[i].

        Example:
            >>> Solution().countSmaller([5, 2, 6, 1])
            [2, 1, 1, 0]
        """
        # TODO: implement using Count Inversions (merge sort)
        pass


if __name__ == "__main__":
    print(Solution().countSmaller([5, 2, 6, 1]))  # expected: [2, 1, 1, 0]
    print(Solution().countSmaller([-1, -1]))      # expected: [0, 0]
