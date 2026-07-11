from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotate an n x n matrix 90 degrees clockwise, in place.

        The matrix is modified directly and nothing is returned. No second
        2-D matrix may be allocated (O(1) auxiliary space).

        Args:
            matrix: An n x n grid of integers, n >= 1. Mutated in place.

        Returns:
            None. The rotation is applied to ``matrix`` itself.

        Example:
            >>> m = [[1, 2], [3, 4]]
            >>> Solution().rotate(m)
            >>> m
            [[3, 1], [4, 2]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(m1)
    print(m1)
    # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    m2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(m2)
    print(m2)
    # Expected: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
