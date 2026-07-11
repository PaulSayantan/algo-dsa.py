from typing import List


class Solution:
    def diagonal_order(self, mat: List[List[int]]) -> List[int]:
        """Return all elements of ``mat`` read one anti-diagonal at a time.

        Diagonals are grouped by the constant ``i + j`` and processed in
        increasing order of that sum. Within each diagonal, cells are emitted
        in increasing order of row index (top-to-bottom).

        Args:
            mat: An ``m x n`` matrix of integers with ``m, n >= 1``.

        Returns:
            A flat list of every element, ordered anti-diagonal by
            anti-diagonal.

        Example:
            >>> Solution().diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            [1, 2, 4, 3, 5, 7, 6, 8, 9]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    print(sol.diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # Expected: [1, 2, 4, 3, 5, 7, 6, 8, 9]

    print(sol.diagonal_order([[1, 2], [3, 4]]))
    # Expected: [1, 2, 3, 4]

    print(sol.diagonal_order([[1, 2, 3, 4]]))
    # Expected: [1, 2, 3, 4]
