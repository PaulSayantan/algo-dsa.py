"""LeetCode 315 — Count of Smaller Numbers After Self, via a Merge Sort Tree.

Fill in the implementation. Build a Merge Sort Tree over nums, then for each index i
count how many elements in the suffix nums[i+1 .. n-1] are strictly less than nums[i]
by binary searching (bisect_left) inside each covering node's sorted list.
"""

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """For each index, count strictly-smaller elements to its right.

        Args:
            nums: The input integer array.

        Returns:
            counts, where counts[i] = number of j > i with nums[j] < nums[i].

        Example:
            >>> Solution().countSmaller([5, 2, 6, 1])
            [2, 1, 1, 0]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().countSmaller([5, 2, 6, 1]))
    # Expected output: [2, 1, 1, 0]
    print(Solution().countSmaller([-1, -1]))
    # Expected output: [0, 0]
