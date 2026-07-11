from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """Return cells from which water can reach both oceans.

        The Pacific touches the top and left edges; the Atlantic touches the
        bottom and right edges. Water flows 4-directionally from a cell to a
        neighbor of height less than or equal to the current cell's height.

        Args:
            heights: An m x n matrix of non-negative cell heights.

        Returns:
            A list of [row, col] coordinates from which water can flow to both
            the Pacific and Atlantic oceans (any order is acceptable).

        Example:
            >>> Solution().pacificAtlantic([[1,2,2,3,5],
            ...                             [3,2,3,4,4],
            ...                             [2,4,5,3,1],
            ...                             [6,7,1,4,5],
            ...                             [5,1,1,2,4]])
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    print(sol.pacificAtlantic(heights))
    # Expected (any order):
    # [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    print(sol.pacificAtlantic([[1]]))
    # Expected: [[0, 0]]
