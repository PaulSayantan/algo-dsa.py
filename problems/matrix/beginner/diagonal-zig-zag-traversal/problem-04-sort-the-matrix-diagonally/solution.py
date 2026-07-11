from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """Sort every ``\\`` diagonal of ``mat`` in ascending order.

        Cells on a diagonal share the constant ``i - j``. Each diagonal is
        sorted independently; values never move between diagonals.

        Args:
            mat: An ``m x n`` matrix of integers with ``m, n >= 1``.

        Returns:
            The matrix with each main (``\\``) diagonal sorted ascending from
            top-left to bottom-right.

        Example:
            >>> Solution().diagonalSort(
            ...     [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]])
            [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    print(sol.diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))
    # Expected: [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]

    print(sol.diagonalSort([[11, 25, 66, 1, 69, 7],
                            [23, 55, 17, 45, 15, 52],
                            [75, 31, 36, 44, 58, 8],
                            [22, 27, 33, 25, 68, 4],
                            [84, 28, 14, 11, 5, 50]]))
    # Expected: [[5, 17, 4, 1, 52, 7],
    #            [11, 11, 25, 45, 8, 69],
    #            [14, 23, 25, 44, 58, 15],
    #            [22, 27, 31, 36, 50, 66],
    #            [84, 28, 75, 33, 55, 68]]

    print(sol.diagonalSort([[1]]))
    # Expected: [[1]]
