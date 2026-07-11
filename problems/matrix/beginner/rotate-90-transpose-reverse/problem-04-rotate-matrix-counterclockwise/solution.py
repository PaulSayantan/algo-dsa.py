"""Rotate Matrix Counter-Clockwise (90 degrees anti-clockwise, in place).

Empty solution template — implement the logic yourself.
"""

from typing import List


class Solution:
    def rotateCounterClockwise(self, matrix: List[List[int]]) -> None:
        """Rotate an ``n x n`` matrix 90 degrees counter-clockwise, in place.

        Modifies ``matrix`` directly and returns nothing.

        Args:
            matrix: An ``n x n`` 2D list to rotate in place.

        Returns:
            None. The rotation is performed on ``matrix`` itself.

        Example:
            >>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            >>> Solution().rotateCounterClockwise(m)
            >>> m
            [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotateCounterClockwise(m)
    print(m)
    # Expected: [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

    m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    Solution().rotateCounterClockwise(m2)
    print(m2)
    # Expected: [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]
