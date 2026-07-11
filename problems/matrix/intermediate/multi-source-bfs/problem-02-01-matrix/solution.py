"""01 Matrix — LeetCode 542.

Empty solution template. Fill in `updateMatrix`.
"""

from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """Return a matrix where each cell holds its distance to the nearest 0.

        Distance is measured in 4-directional steps between adjacent cells. Cells that
        already contain 0 have distance 0.

        Args:
            mat: An m x n binary matrix containing 0s and 1s, with at least one 0.

        Returns:
            An m x n matrix of the same shape; each entry is the number of steps to
            the closest cell containing a 0.

        Example:
            >>> Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
            [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        """
        # TODO: implement using Multi-Source BFS.
        pass


if __name__ == "__main__":
    print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    # Expected: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
    # Expected: [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
