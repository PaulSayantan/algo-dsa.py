"""Determine Whether Matrix Can Be Obtained By Rotation (LeetCode 1886).

Empty solution template — implement the logic yourself.
"""

from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """Return True if some number of 90-degree rotations makes mat == target.

        Args:
            mat: An ``n x n`` binary matrix to rotate.
            target: An ``n x n`` binary matrix to match.

        Returns:
            True if rotating ``mat`` by 0, 1, 2, or 3 quarter-turns can equal
            ``target``; otherwise False.

        Example:
            >>> Solution().findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]])
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]))
    # Expected: True

    print(Solution().findRotation([[0, 1], [1, 1]], [[1, 0], [0, 1]]))
    # Expected: False
