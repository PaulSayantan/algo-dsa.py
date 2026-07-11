"""Count Subtrees With Max Distance Between Cities.

LeetCode 1617. Precompute all-pairs tree distances with Floyd–Warshall, then
enumerate subsets of cities.
"""

from typing import List


class Solution:
    def countSubgraphsForEachDiameter(
        self,
        n: int,
        edges: List[List[int]],
    ) -> List[int]:
        """Count, for each d in 1..n-1, the number of connected subtrees with diameter d.

        The cities form a tree. Precompute every pairwise distance with Floyd–Warshall.
        Then enumerate all 2^n city subsets; a subset is a valid subtree iff it has at
        least 2 cities and its induced subgraph is connected (equivalently, it contains
        exactly (size - 1) of the tree edges). For each valid subtree, its diameter is
        the maximum pairwise distance among its cities; increment the count for that d.

        Args:
            n: Number of cities, labeled ``1 .. n``.
            edges: The ``n - 1`` bidirectional edges forming the tree.

        Returns:
            A list of length ``n - 1`` where index ``d - 1`` holds the number of
            subtrees whose maximum inter-city distance equals ``d``.

        Example:
            >>> Solution().countSubgraphsForEachDiameter(4, [[1, 2], [2, 3], [2, 4]])
            [3, 4, 0]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubgraphsForEachDiameter(4, [[1, 2], [2, 3], [2, 4]]))
    # Expected: [3, 4, 0]
    print(sol.countSubgraphsForEachDiameter(2, [[1, 2]]))
    # Expected: [1]
    print(sol.countSubgraphsForEachDiameter(3, [[1, 2], [2, 3]]))
    # Expected: [2, 1]
