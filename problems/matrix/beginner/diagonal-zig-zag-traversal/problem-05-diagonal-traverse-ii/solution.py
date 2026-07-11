from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """Return all elements of a jagged 2D array in diagonal order.

        Cells are grouped by the anti-diagonal key ``i + j`` and diagonals are
        emitted in increasing order of that key. Within a diagonal, cells are
        read bottom-to-top (decreasing row index). Rows may have different
        lengths.

        Args:
            nums: A jagged list of integer lists, each with length >= 1.

        Returns:
            A flat list of every element in diagonal order.

        Example:
            >>> Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            [1, 4, 2, 7, 5, 3, 8, 6, 9]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    print(sol.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # Expected: [1, 4, 2, 7, 5, 3, 8, 6, 9]

    print(sol.findDiagonalOrder([[1, 2, 3, 4, 5],
                                 [6, 7],
                                 [8],
                                 [9, 10, 11],
                                 [12, 13, 14, 15, 16]]))
    # Expected: [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]
