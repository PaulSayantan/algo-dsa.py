"""Evaluate Division.

LeetCode 399. Solve with a multiplicative Floyd–Warshall over the variable graph.
"""

from typing import List


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        """Evaluate each query C / D given a set of A / B = value equations.

        Assign each distinct variable an index, then build a ratio matrix where
        ``ratio[i][j]`` is the value of ``var_i / var_j``. Seed it from the equations
        (with reciprocals for the reverse direction), then run Floyd–Warshall using
        multiplication to propagate ratios along paths. Answer -1.0 for any query whose
        variables are unknown or lie in disconnected components.

        Args:
            equations: List of ``[A, B]`` variable pairs.
            values: ``values[i]`` is the value of ``equations[i][0] / equations[i][1]``.
            queries: List of ``[C, D]`` pairs to evaluate as ``C / D``.

        Returns:
            A list of floats, one per query; -1.0 where the ratio cannot be determined.

        Example:
            >>> Solution().calcEquation(
            ...     [["a", "b"], ["b", "c"]], [2.0, 3.0],
            ...     [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            ... )
            [6.0, 0.5, -1.0, 1.0, -1.0]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.calcEquation(
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        )
    )
    # Expected: [6.0, 0.5, -1.0, 1.0, -1.0]
    print(
        sol.calcEquation(
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
        )
    )
    # Expected: [3.75, 0.4, 5.0, 0.2]
