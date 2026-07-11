"""Find K Closest Elements (LeetCode 658).

Return the k integers closest to x from a sorted array, in ascending order.
Ties are broken toward the smaller value.
"""
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """Return the ``k`` elements of ``arr`` closest to ``x``, sorted ascending.

        Closeness is measured by ``abs(a - x)``; ties break toward the smaller
        value (``a < b``).

        Args:
            arr: A list of integers sorted in ascending order (duplicates allowed).
            k: The number of closest elements to return (``1 <= k <= len(arr)``).
            x: The reference value to measure distance from.

        Returns:
            A list of exactly ``k`` integers, sorted in ascending order, that are
            the closest values to ``x`` in ``arr``.

        Example:
            >>> Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3)
            [1, 2, 3, 4]
            >>> Solution().findClosestElements([2, 3, 7, 8], 1, 6)
            [7]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # Expected: [1, 2, 3, 4]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 3))
    # Expected: [1, 2, 3, 4]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, -1))
    # Expected: [7]
    print(sol.findClosestElements([2, 3, 7, 8], 1, 6))
