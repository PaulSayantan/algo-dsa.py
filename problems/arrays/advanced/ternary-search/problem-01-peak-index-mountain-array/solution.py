"""Peak Index in a Mountain Array (LeetCode 852) via integer Ternary Search.

Fill in `peakIndexInMountainArray` to return the index of the single peak of a
strictly-increasing-then-strictly-decreasing array in O(log n) time.
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """Return the index of the peak element of a mountain array.

        The array first strictly increases, then strictly decreases, so
        f(index) = arr[index] is unimodal. Use integer ternary search on the
        index range [0, len(arr) - 1] to locate the argmax.

        Args:
            arr: A mountain array (len >= 3, strictly up then strictly down).

        Returns:
            The index i of the peak, i.e. the argmax of arr.

        Example:
            >>> Solution().peakIndexInMountainArray([0, 2, 4, 6, 5, 3, 1])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.peakIndexInMountainArray([0, 1, 0]))            # Expected: 1
    print(sol.peakIndexInMountainArray([0, 2, 4, 6, 5, 3, 1]))  # Expected: 3
    print(sol.peakIndexInMountainArray([3, 4, 5, 1]))         # Expected: 2
