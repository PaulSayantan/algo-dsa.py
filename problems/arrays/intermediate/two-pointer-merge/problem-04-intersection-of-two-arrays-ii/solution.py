"""LeetCode 350 - Intersection of Two Arrays II.

Return the multiset intersection. The intended optimization (per the follow-up)
sorts both arrays and then applies the Two-Pointer Merge technique. Fill in
`intersect`.
"""

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Return the multiset intersection of nums1 and nums2.

        Each value appears min(count_in_nums1, count_in_nums2) times. The order
        of the result does not matter.

        Args:
            nums1: First list of integers.
            nums2: Second list of integers.

        Returns:
            A list containing the intersection, with correct multiplicities.

        Example:
            >>> Solution().intersect([1, 2, 2, 1], [2, 2])
            [2, 2]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()

    print(s.intersect([1, 2, 2, 1], [2, 2]))          # expected: [2, 2]
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))    # expected: [4, 9] (any order)
    print(s.intersect([1, 2, 3], [4, 5, 6]))          # expected: []
