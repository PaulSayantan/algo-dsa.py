"""Intersection of Two Arrays II (LeetCode 350).

Return the multiset intersection: each value appears min(count1, count2) times.
"""

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Return the intersection of two arrays, preserving multiplicities.

        A value that occurs ``a`` times in ``nums1`` and ``b`` times in
        ``nums2`` appears ``min(a, b)`` times in the result. The order of the
        returned elements does not matter.

        Args:
            nums1: The first list of integers.
            nums2: The second list of integers.

        Returns:
            A list containing the multiset intersection of the two inputs.

        Example:
            >>> sorted(Solution().intersect([1, 2, 2, 1], [2, 2]))
            [2, 2]
            >>> sorted(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))
            [4, 9]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    solver = Solution()

    print(solver.intersect([1, 2, 2, 1], [2, 2]))  # expected: [2, 2]
    print(solver.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # expected: [4, 9] (any order)
    print(solver.intersect([1, 2, 2, 1], [3, 4]))  # expected: []
