from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """Return minutes until no fresh orange remains, or -1 if impossible.

        Each minute, every fresh orange (1) adjacent 4-directionally to a rotten
        orange (2) becomes rotten. 0 marks an empty cell.

        Args:
            grid: An m x n grid with values 0 (empty), 1 (fresh), 2 (rotten).

        Returns:
            The minimum number of minutes for all reachable fresh oranges to
            rot, or -1 if at least one fresh orange can never rot.

        Example:
            >>> Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    # Expected: 4
    print(sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    # Expected: -1
    print(sol.orangesRotting([[0, 2]]))
    # Expected: 0
