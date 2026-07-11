from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """Return the elements of ``mat`` in diagonal zig-zag order.

        Anti-diagonals (grouped by the constant ``i + j``) are emitted in
        alternating direction: even-indexed diagonals go up-right
        (bottom-to-top) and odd-indexed diagonals go down-left
        (top-to-bottom).

        Args:
            mat: An ``m x n`` matrix of integers with ``m, n >= 1``.

        Returns:
            A flat list of every element in diagonal zig-zag order.

        Example:
            >>> Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            [1, 2, 4, 7, 5, 3, 6, 8, 9]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    print(sol.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # Expected: [1, 2, 4, 7, 5, 3, 6, 8, 9]

    print(sol.findDiagonalOrder([[1, 2], [3, 4]]))
    # Expected: [1, 2, 3, 4]

    print(sol.findDiagonalOrder([[1], [2], [3]]))
    # Expected: [1, 2, 3]
