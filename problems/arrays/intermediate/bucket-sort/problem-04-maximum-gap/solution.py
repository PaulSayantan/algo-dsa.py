"""LeetCode 164 - Maximum Gap.

Fill in the body of `maximumGap` using Bucket Sort / the pigeonhole principle.
"""

from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """Return the maximum gap between successive elements of sorted ``nums``.

        Must run in O(n) time and O(n) space.

        Args:
            nums: The input array of non-negative integers.

        Returns:
            The largest difference between two consecutive values once the array
            is sorted, or 0 if there are fewer than two elements.

        Example:
            >>> Solution().maximumGap([3, 6, 9, 1])
            3
        """
        # TODO: implement using bucket sort (pigeonhole buckets with min/max)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumGap([3, 6, 9, 1]))    # expected: 3
    print(sol.maximumGap([10]))            # expected: 0
    print(sol.maximumGap([1, 10, 5, 3]))   # expected: 5
