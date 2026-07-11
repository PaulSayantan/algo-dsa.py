from typing import List


class Solution:
    def rotateCounterclockwise(self, matrix: List[List[int]]) -> None:
        """Rotate an n x n matrix 90 degrees counterclockwise, in place.

        The matrix is modified directly and nothing is returned. No second
        2-D matrix may be allocated (O(1) auxiliary space).

        Args:
            matrix: An n x n grid of integers, n >= 1. Mutated in place.

        Returns:
            None. The rotation is applied to ``matrix`` itself.

        Example:
            >>> m = [[1, 2], [3, 4]]
            >>> Solution().rotateCounterclockwise(m)
            >>> m
            [[2, 4], [1, 3]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotateCounterclockwise(m1)
    print(m1)
    # Expected: [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

    m2 = [[1, 2], [3, 4]]
    sol.rotateCounterclockwise(m2)
    print(m2)
    # Expected: [[2, 4], [1, 3]]
