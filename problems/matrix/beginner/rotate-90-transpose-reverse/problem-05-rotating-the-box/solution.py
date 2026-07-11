"""Rotating the Box (LeetCode 1861).

Empty solution template — implement the logic yourself.
"""

from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """Apply gravity, then rotate the box 90 degrees clockwise.

        Args:
            box: An ``m x n`` grid of characters where each cell is
                ``'#'`` (stone), ``'*'`` (obstacle), or ``'.'`` (empty).

        Returns:
            An ``n x m`` grid representing the box after gravity settles the
            stones and the box is rotated 90 degrees clockwise.

        Example:
            >>> Solution().rotateTheBox([["#", ".", "#"]])
            [['.'], ['#'], ['#']]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().rotateTheBox([["#", ".", "#"]]))
    # Expected: [['.'], ['#'], ['#']]

    print(Solution().rotateTheBox([["#", ".", "*", "."], ["#", "#", "*", "."]]))
    # Expected: [['#', '.'], ['#', '#'], ['*', '*'], ['.', '.']]
