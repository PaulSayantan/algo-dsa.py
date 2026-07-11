"""Campus Bikes II (LeetCode 1066) — empty solution template.

Build a Manhattan-distance cost matrix (workers x bikes, workers <= bikes) and
run the Hungarian Algorithm to minimize the total assigned distance. Do NOT
hard-code answers.
"""

from typing import List


class Solution:
    def assignBikes(
        self, workers: List[List[int]], bikes: List[List[int]]
    ) -> int:
        """Return the minimum total Manhattan distance of a worker-to-bike assignment.

        Args:
            workers: List of ``[x, y]`` worker coordinates (length ``n``).
            bikes: List of ``[x, y]`` bike coordinates (length ``m``, ``m >= n``).

        Returns:
            The minimum achievable sum of Manhattan distances when every worker
            is given a distinct bike.

        Example:
            >>> Solution().assignBikes([[0, 0], [2, 1]], [[1, 2], [3, 3]])
            6
        """
        # TODO: implement.
        #   1) cost[i][j] = |wx - bx| + |wy - by|
        #   2) pad to square (dummy bikes) or use an n<=m Hungarian variant
        #   3) return the minimum total cost
        pass


if __name__ == "__main__":
    workers = [[0, 0], [2, 1]]
    bikes = [[1, 2], [3, 3]]
    print(Solution().assignBikes(workers, bikes))  # Expected: 6

    workers2 = [[0, 0], [1, 1], [2, 0]]
    bikes2 = [[1, 0], [2, 2], [2, 1]]
    print(Solution().assignBikes(workers2, bikes2))  # Expected: 4
