"""Max Value of Equation — LeetCode 1499.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """Return the max of y_i + y_j + |x_i - x_j| over valid pairs.

        Points are given sorted by strictly increasing x. A pair ``(i, j)`` with
        ``i < j`` is valid when ``|x_i - x_j| <= k``.

        Args:
            points: List of ``[x, y]`` coordinates, sorted by increasing ``x``.
            k: The maximum allowed absolute x-distance between a chosen pair.

        Returns:
            The maximum value of ``y_i + y_j + |x_i - x_j|`` over all valid pairs.

        Example:
            >>> Solution().findMaxValueOfEquation([[1, 3], [2, 0], [5, 10], [6, -10]], 1)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxValueOfEquation([[1, 3], [2, 0], [5, 10], [6, -10]], 1))
    # expected: 4
    print(sol.findMaxValueOfEquation([[0, 0], [3, 0], [9, 2]], 3))  # expected: 3
