from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotate an ``n x n`` matrix 90 degrees clockwise, in place.

        Args:
            matrix: A square 2D list. Modified in place; no new matrix is
                allocated.

        Returns:
            None. ``matrix`` is mutated to its 90-degree clockwise rotation.

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
    print(m)  # expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
