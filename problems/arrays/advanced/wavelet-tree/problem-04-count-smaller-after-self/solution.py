"""LeetCode 315 - Count of Smaller Numbers After Self, via a Wavelet Tree.

Build a Wavelet Tree over `nums`, then for each i count values < nums[i] in the
suffix nums[i+1 .. n) using a range 'count of values <= x' query.
"""

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """For each index i, count elements to its right that are smaller.

        Args:
            nums: The input integer array (length n, 1 <= n <= 1e5).

        Returns:
            A list `counts` of length n where counts[i] = number of j with
            i < j < n and nums[j] < nums[i].

        Example:
            >>> Solution().countSmaller([5, 2, 6, 1])
            [2, 1, 1, 0]
        """
        # TODO: implement
        # Hint: build a Wavelet Tree over nums; for each i return the count of
        #       values <= nums[i] - 1 within the suffix window [i + 1, n).
        pass


if __name__ == "__main__":
    print(Solution().countSmaller([5, 2, 6, 1]))  # expected: [2, 1, 1, 0]
    print(Solution().countSmaller([-1, -1]))       # expected: [0, 0]
    print(Solution().countSmaller([3]))            # expected: [0]
