"""LeetCode 315 - Count of Smaller Numbers After Self.

Fill in the body using a Binary Indexed Tree (Fenwick Tree) over
coordinate-compressed values, sweeping the array from right to left.
"""

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """Count, for each index, how many later elements are strictly smaller.

        Args:
            nums: The input integer array.

        Returns:
            A list `counts` where counts[i] is the number of j > i with
            nums[j] < nums[i].

        Example:
            >>> Solution().countSmaller([5, 2, 6, 1])
            [2, 1, 1, 0]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSmaller([5, 2, 6, 1]))     # expected: [2, 1, 1, 0]
    print(sol.countSmaller([-1, -1]))         # expected: [0, 0]
    print(sol.countSmaller([7, 6, 5, 4, 3]))  # expected: [4, 3, 2, 1, 0]
