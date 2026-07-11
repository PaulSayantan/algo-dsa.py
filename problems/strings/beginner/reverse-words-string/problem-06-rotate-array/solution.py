"""LeetCode 189 - Rotate Array.

Rotate an integer array to the right by k steps in place, using the reversal
identity (reverse whole, then reverse the two parts).
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Rotate `nums` to the right by `k` steps, in place.

        Args:
            nums: The integer array to rotate. Modified in place.
            k: A non-negative number of right-rotation steps. May exceed
               len(nums), in which case it wraps around.

        Returns:
            None. The rotation is applied to `nums` in place.

        Example:
            >>> arr = [1, 2, 3, 4, 5, 6, 7]
            >>> Solution().rotate(arr, 3)
            >>> arr
            [5, 6, 7, 1, 2, 3, 4]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(arr, 3)
    print(arr)  # expected: [5, 6, 7, 1, 2, 3, 4]

    arr2 = [-1, -100, 3, 99]
    Solution().rotate(arr2, 2)
    print(arr2)  # expected: [3, 99, -1, -100]
