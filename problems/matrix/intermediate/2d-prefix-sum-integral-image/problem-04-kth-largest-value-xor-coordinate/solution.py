"""Find Kth Largest XOR Coordinate Value (LeetCode 1738).

Fill in the body of kthLargestValue. Do not change the signature.
"""

from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        """Return the k-th largest XOR-prefix coordinate value.

        The value at (a, b) is the XOR of all matrix[i][j] with i <= a and
        j <= b. Return the k-th largest such value (1-indexed).

        Args:
            matrix: An m x n matrix of non-negative integers.
            k: 1-indexed rank of the value to return (1 <= k <= m * n).

        Returns:
            The k-th largest coordinate value.

        Example:
            >>> Solution().kthLargestValue([[5, 2], [1, 6]], 1)
            7
            >>> Solution().kthLargestValue([[5, 2], [1, 6]], 3)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().kthLargestValue([[5, 2], [1, 6]], 1))  # expected 7
    print(Solution().kthLargestValue([[5, 2], [1, 6]], 3))  # expected 4
    print(Solution().kthLargestValue([[5, 2], [1, 6]], 4))  # expected 0
