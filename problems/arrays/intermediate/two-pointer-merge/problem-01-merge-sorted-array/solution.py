"""LeetCode 88 - Merge Sorted Array.

Merge two sorted arrays in place. Fill in `merge` using the Two-Pointer Merge
technique. Do not use a library sort as the intended solution.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Merge nums2 into nums1 in place so nums1 becomes sorted.

        Args:
            nums1: List of length m + n. The first m entries are sorted values;
                the trailing n entries are placeholder zeros to be overwritten.
            m: Number of real elements at the start of nums1.
            nums2: Sorted list of length n.
            n: Number of elements in nums2.

        Returns:
            None. The result is written in place into nums1.

        Example:
            >>> s = Solution()
            >>> a = [1, 2, 3, 0, 0, 0]
            >>> s.merge(a, 3, [2, 5, 6], 3)
            >>> a
            [1, 2, 2, 3, 5, 6]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    s.merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)  # expected: [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    s.merge(nums1, 1, [], 0)
    print(nums1)  # expected: [1]

    nums1 = [0]
    s.merge(nums1, 0, [1], 1)
    print(nums1)  # expected: [1]
