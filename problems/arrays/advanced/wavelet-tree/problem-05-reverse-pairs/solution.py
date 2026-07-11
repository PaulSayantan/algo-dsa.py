"""LeetCode 493 - Reverse Pairs, via a Wavelet Tree.

Build a Wavelet Tree over `nums`. For each j, the number of i < j with
nums[i] > 2 * nums[j] equals the count of prefix values in [0, j) that are
strictly greater than 2 * nums[j].
"""

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """Count pairs (i, j) with i < j and nums[i] > 2 * nums[j].

        Args:
            nums: The input integer array (length n, 1 <= n <= 5e4). Values may
                be as large as +/- 2^31 - 1, so 2 * nums[j] can exceed 32 bits.

        Returns:
            The number of important reverse pairs.

        Example:
            >>> Solution().reversePairs([1, 3, 2, 3, 1])
            2
        """
        # TODO: implement
        # Hint: build a Wavelet Tree over nums; sweep j left to right and add
        #       (count of values in [0, j) strictly greater than 2 * nums[j]),
        #       i.e. j - range_count_leq(0, j, 2 * nums[j]).
        pass


if __name__ == "__main__":
    print(Solution().reversePairs([1, 3, 2, 3, 1]))  # expected: 2
    print(Solution().reversePairs([2, 4, 3, 5, 1]))  # expected: 3
