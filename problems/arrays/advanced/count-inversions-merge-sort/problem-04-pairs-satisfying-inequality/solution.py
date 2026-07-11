"""Number of Pairs Satisfying Inequality (LeetCode 2426).

Fill in `Solution.numberOfPairs`. Build the derived array
d[k] = nums1[k] - nums2[k] and count pairs i < j with d[i] <= d[j] + diff
using the merge-sort counting technique.
"""
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        """Count pairs (i, j), i < j, with nums1[i]-nums1[j] <= nums2[i]-nums2[j]+diff.

        Args:
            nums1: First integer array of length n.
            nums2: Second integer array of length n (same length as nums1).
            diff: Integer slack added to the right-hand side.

        Returns:
            The number of valid pairs as an integer.

        Example:
            >>> Solution().numberOfPairs([3, 2, 5], [2, 2, 1], 1)
            3
        """
        # TODO: implement using Count Inversions (merge sort)
        pass


if __name__ == "__main__":
    print(Solution().numberOfPairs([3, 2, 5], [2, 2, 1], 1))    # expected: 3
    print(Solution().numberOfPairs([3, -1], [-2, 2], -1))       # expected: 0
