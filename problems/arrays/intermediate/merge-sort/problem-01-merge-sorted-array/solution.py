from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Merge the sorted array nums2 into the sorted array nums1 in place.

        The first ``m`` entries of ``nums1`` hold its real values; the trailing
        ``n`` entries are placeholder zeros. After the call, ``nums1`` must hold
        all ``m + n`` values in non-decreasing order.

        Args:
            nums1: Sorted list of length ``m + n``; first ``m`` entries valid.
            m: Number of valid elements in ``nums1``.
            nums2: Sorted list of length ``n``.
            n: Number of elements in ``nums2``.

        Returns:
            None. ``nums1`` is modified in place.

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

    a = [1, 2, 3, 0, 0, 0]
    s.merge(a, 3, [2, 5, 6], 3)
    print(a)  # expected: [1, 2, 2, 3, 5, 6]

    b = [1]
    s.merge(b, 1, [], 0)
    print(b)  # expected: [1]

    c = [0]
    s.merge(c, 0, [1], 1)
    print(c)  # expected: [1]
