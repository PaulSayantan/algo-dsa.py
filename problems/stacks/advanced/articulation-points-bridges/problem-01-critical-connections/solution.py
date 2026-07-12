"""Critical Connections in a Network — LeetCode 1192."""
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # TODO: bridge-finding DFS with discovery/low arrays
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))  # expected: [[1, 3]]
    print(sol.criticalConnections(2, [[0, 1]]))  # expected: [[0, 1]]
    print(sol.criticalConnections(6, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]))  # expected: [[1, 3]]
