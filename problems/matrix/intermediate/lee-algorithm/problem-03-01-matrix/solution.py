"""01 Matrix (LeetCode 542).

Fill in the body using the multi-source Lee Algorithm (BFS). Do not modify the
signature.
"""
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """Return a matrix of distances from each cell to its nearest 0.

        Distance is measured in 4-directional steps. Cells that are already 0
        have distance 0.

        Args:
            mat: An m x n binary matrix. Guaranteed to contain at least one 0.

        Returns:
            An m x n matrix where entry (i, j) is the number of steps from
            (i, j) to the closest cell containing 0.

        Example:
            >>> Solution().updateMatrix([[0, 0, 0],
            ...                          [0, 1, 0],
            ...                          [1, 1, 1]])
            [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.updateMatrix([[0, 0, 0],
                            [0, 1, 0],
                            [0, 0, 0]]))
    # expected: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(sol.updateMatrix([[0, 0, 0],
                            [0, 1, 0],
                            [1, 1, 1]]))
    # expected: [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
