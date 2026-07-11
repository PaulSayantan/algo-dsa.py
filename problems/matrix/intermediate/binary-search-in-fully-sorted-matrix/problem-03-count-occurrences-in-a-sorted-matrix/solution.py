"""Count Occurrences in a Sorted Matrix.

Empty solution template — fill in the body yourself.
"""
from typing import List


class Solution:
    def countOccurrences(self, matrix: List[List[int]], target: int) -> int:
        """Count how many times ``target`` appears in a row-major sorted matrix.

        Treat the matrix as a virtual sorted array of ``m * n`` elements. Binary
        search for ``lower_bound(target)`` (first flat index whose value is
        ``>= target``) and ``upper_bound(target)`` (first flat index whose value
        is ``> target``); the count is their difference. Map a flat index ``idx``
        to the cell ``matrix[idx // n][idx % n]``.

        Args:
            matrix: An ``m x n`` grid sorted in row-major order (duplicates ok).
            target: The integer value to count.

        Returns:
            The number of occurrences of ``target`` in ``matrix`` (0 if absent).

        Example:
            >>> Solution().countOccurrences([[1, 1, 2], [2, 2, 3]], 2)
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().countOccurrences([[1, 1, 2], [2, 2, 3]], 2))  # expected: 3
    print(Solution().countOccurrences([[1, 1, 2], [2, 2, 3]], 5))  # expected: 0
    print(Solution().countOccurrences([[4, 4], [4, 4]], 4))        # expected: 4
