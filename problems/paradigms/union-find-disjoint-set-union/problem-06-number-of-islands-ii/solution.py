"""LeetCode 305 - Number of Islands II.

Fill in the body of `numIslands2`. The intended technique is an online
Union-Find (Disjoint Set Union): each added land cell starts a new island,
then merges with any orthogonally adjacent land cell.
"""
from typing import List


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """Return the island count after each add-land operation.

        Args:
            m: Number of rows in the grid.
            n: Number of columns in the grid.
            positions: The sequence of [r, c] cells to turn into land, in
                order. Positions may repeat.

        Returns:
            A list `answer` where answer[i] is the number of islands right
            after processing positions[i].

        Example:
            >>> Solution().numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]])
            [1, 1, 2, 3]
        """
        # TODO: implement using Union-Find (Disjoint Set Union)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))  # expected: [1, 1, 2, 3]
    print(sol.numIslands2(2, 2, [[0, 0], [1, 1], [0, 1]]))          # expected: [1, 2, 1]
    print(sol.numIslands2(1, 1, [[0, 0]]))                          # expected: [1]
