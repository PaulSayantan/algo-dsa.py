"""Maximum Length of Repeated Subarray (LeetCode 718).

Find the longest contiguous subarray common to nums1 and nums2 using binary
search on the length plus a polynomial rolling hash for each check.
"""

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """Return the maximum length of a subarray present in both arrays.

        Args:
            nums1: First integer array.
            nums2: Second integer array.

        Returns:
            The length of the longest contiguous subarray that appears in both
            ``nums1`` and ``nums2`` (0 if none).

        Example:
            >>> Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
            3
            >>> Solution().findLength([1, 2, 3], [4, 5, 6])
            0
        """
        # TODO: implement with binary search on length + rolling hash.
        #   - has_common(L): hash all length-L windows of nums1 into a set, then
        #     scan nums2's length-L windows for a hit (verify on collision).
        #   - Binary search the largest L in [0, min(len1, len2)] for which
        #     has_common(L) is True.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # expected: 3
    print(sol.findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))  # expected: 5
    print(sol.findLength([1, 2, 3], [4, 5, 6]))              # expected: 0
