"""Falling Squares (LeetCode 699).

Fill in the segment-tree-with-lazy-propagation logic (range-assign + range-max
over coordinate-compressed X positions). Keep the LeetCode-style signature below
unchanged.
"""
from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        """Return the running max stack height after each square lands.

        Args:
            positions: Each entry is [left, sideLength]; the square occupies the
                X-interval [left, left + sideLength] and has height sideLength.

        Returns:
            A list where the i-th value is the height of the tallest stack after
            the i-th square has landed.

        Example:
            Solution().fallingSquares([[1,2],[2,3],[6,1]])  # -> [2, 5, 5]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.fallingSquares([[1, 2], [2, 3], [6, 1]]))      # expected: [2, 5, 5]
    print(sol.fallingSquares([[100, 100], [200, 100]]))      # expected: [100, 100]
