from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """Count the negative numbers in a doubly non-increasing sorted matrix.

        Each row and each column is sorted in non-increasing order, so the
        negatives occupy a bottom-right staircase region. Aim for O(m + n) time
        and O(1) extra space with a saddleback walk.

        Args:
            grid: An ``m x n`` matrix, each row and column sorted in
                non-increasing (largest-to-smallest) order.

        Returns:
            The count of entries in ``grid`` that are strictly less than 0.

        Example:
            >>> Solution().countNegatives([[3, 2], [1, 0]])
            0
            >>> Solution().countNegatives([[1, -1], [-1, -1]])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    g = [
        [4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3],
    ]
    print(Solution().countNegatives(g))            # expected: 8
    print(Solution().countNegatives([[3, 2], [1, 0]]))  # expected: 0
