"""Best Position for a Service Centre (LeetCode 1515) via nested Ternary Search.

Fill in `getMinDistSum` to return the minimum sum of Euclidean distances from a
chosen point to all given positions (the geometric median's cost).
"""

from typing import List


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        """Minimize the total Euclidean distance to all positions.

        cost(x, y) = sum_i sqrt((x - x_i)^2 + (y - y_i)^2) is convex in (x, y),
        hence unimodal along each axis. Use an outer ternary search over x whose
        evaluation is an inner ternary search over the best y for that x.

        Args:
            positions: List of [x_i, y_i] integer customer coordinates.

        Returns:
            The minimum achievable sum of distances, accurate to ~1e-5.

        Example:
            >>> round(Solution().getMinDistSum([[0, 1], [1, 0], [1, 2], [2, 1]]), 5)
            4.0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(round(sol.getMinDistSum([[0, 1], [1, 0], [1, 2], [2, 1]]), 5))  # Expected: 4.0
    print(round(sol.getMinDistSum([[1, 1], [3, 3]]), 5))                   # Expected: 2.82843
    print(round(sol.getMinDistSum([[1, 1]]), 5))                           # Expected: 0.0
