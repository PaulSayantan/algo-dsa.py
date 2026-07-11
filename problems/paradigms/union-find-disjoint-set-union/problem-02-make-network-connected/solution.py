"""LeetCode 1319 - Number of Operations to Make Network Connected.

Fill in the body of `makeConnected`. The intended technique is
Union-Find (Disjoint Set Union): count connected components, verify there
are enough cables, and return components - 1.
"""
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """Return the minimum number of cable moves to connect all computers.

        Args:
            n: The number of computers, labeled 0 .. n - 1.
            connections: A list of [a, b] pairs, each an existing cable
                directly connecting computers a and b.

        Returns:
            The minimum number of cable relocations needed so that every
            computer is connected (directly or indirectly), or -1 if it is
            impossible because there are not enough cables.

        Example:
            >>> Solution().makeConnected(4, [[0, 1], [0, 2], [1, 2]])
            1
        """
        # TODO: implement using Union-Find (Disjoint Set Union)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.makeConnected(4, [[0, 1], [0, 2], [1, 2]]))              # expected: 1
    print(sol.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))  # expected: 2
    print(sol.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]))      # expected: -1
