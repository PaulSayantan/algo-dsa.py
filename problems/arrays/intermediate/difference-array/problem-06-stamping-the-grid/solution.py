from typing import List


class Solution:
    def possibleToStamp(
        self, grid: List[List[int]], stampHeight: int, stampWidth: int
    ) -> bool:
        """Decide whether stamps can cover every empty cell without hitting a 1.

        A stamp is a stampHeight x stampWidth axis-aligned rectangle placed fully
        inside the grid. Stamps may overlap and may not cover any occupied cell.

        Args:
            grid: An m x n binary matrix; 0 is empty, 1 is occupied.
            stampHeight: The stamp's height in rows.
            stampWidth: The stamp's width in columns.

        Returns:
            True if there is a placement of stamps covering all empty cells while
            avoiding every occupied cell; False otherwise.

        Example:
            >>> Solution().possibleToStamp([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2, 2)
            False
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.possibleToStamp([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 2))  # expected: True
    print(sol.possibleToStamp([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2, 2))  # expected: False
