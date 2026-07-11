"""Cut Off Trees for Golf Event — LeetCode 675.

Empty solution template. Fill in `cutOffTree`.
"""

from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        """Return the minimum total steps to cut all trees in increasing-height order,
        starting from (0, 0), or -1 if some tree cannot be reached.

        Cells: 0 is blocked, 1 is walkable ground, and any value > 1 is a walkable tree
        of that height. Cutting a tree turns its cell into 1. Movement is 4-directional
        between walkable cells (value >= 1).

        Args:
            forest: An m x n grid of non-negative integers with distinct tree heights.

        Returns:
            The minimum number of steps to walk and cut every tree in order, or -1 if
            impossible.

        Example:
            >>> Solution().cutOffTree([[1, 2, 3], [0, 0, 4], [7, 6, 5]])
            6
        """
        # TODO: implement by sorting trees by height, then A* Search for each leg.
        pass


if __name__ == "__main__":
    print(Solution().cutOffTree([[1, 2, 3], [0, 0, 4], [7, 6, 5]]))
    # Expected: 6
    print(Solution().cutOffTree([[1, 2, 3], [0, 0, 0], [7, 6, 5]]))
    # Expected: -1
    print(Solution().cutOffTree([[2, 3, 4], [0, 0, 5], [8, 7, 6]]))
    # Expected: 6
