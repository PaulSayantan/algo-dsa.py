from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotate an n x n matrix 90 degrees clockwise, in place.

        Args:
            matrix: An n x n grid of integers. Modified in place.

        Returns:
            None. The rotation is performed by mutating ``matrix`` directly.

        Example:
            >>> grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            >>> Solution().rotate(grid)
            >>> grid
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(grid)
    print(grid)  # expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
