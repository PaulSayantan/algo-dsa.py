"""LeetCode 684 - Redundant Connection.

Fill in the body of `findRedundantConnection`. The intended technique is
Union-Find (Disjoint Set Union): scan edges in order and return the first
edge whose endpoints already share a root (it closes a cycle).
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """Return the edge that can be removed to leave a valid tree.

        Args:
            edges: A list of undirected edges [a, b] over nodes labeled
                1 .. n. The graph is a tree plus exactly one extra edge.

        Returns:
            The [a, b] edge to remove. If several edges could be removed,
            the one appearing last in `edges`.

        Example:
            >>> Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]])
            [2, 3]
        """
        # TODO: implement using Union-Find (Disjoint Set Union)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))                  # expected: [2, 3]
    print(sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # expected: [1, 4]
