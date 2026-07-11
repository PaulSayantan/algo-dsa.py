"""Rotate Image (LeetCode 48).

Empty solution template — implement the logic yourself.
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotate an ``n x n`` matrix 90 degrees clockwise, in place.

        Modifies ``matrix`` directly and returns nothing.

        Args:
            matrix: An ``n x n`` 2D list to rotate in place.

        Returns:
            None. The rotation is performed on ``matrix`` itself.

        Example:
            >>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            >>> Solution().rotate(m)
            >>> m
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(m)
    print(m)
    # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    m2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution().rotate(m2)
    print(m2)
    # Expected: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
