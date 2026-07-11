"""Escape the Grid — maximum vertex-disjoint paths via node-splitting max-flow.

Fill in `max_escape` using a Max-Flow / Min-Cut on Grid model: split every open
cell into in/out nodes joined by a capacity-1 edge so each cell hosts at most one
path, connect a super source to every 'S' and a super sink to every 'E', and
return the maximum flow.
"""

from typing import List


class Solution:
    def max_escape(self, grid: List[str]) -> int:
        """Return the maximum number of people that can escape with cell-disjoint paths.

        People move between orthogonally adjacent non-wall cells; no cell (including
        start and exit cells) may be shared by two people's paths.

        Args:
            grid: A list of R strings of length C, each character one of
                'S' (person), 'E' (exit), '.' (open floor), '#' (wall).

        Returns:
            The maximum number of people who can simultaneously reach an exit.

        Example:
            >>> Solution().max_escape(["S.E", "S.E"])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.max_escape(["S.E", "S.E"]))          # expected: 2
    print(sol.max_escape(["S.S", "#.#", "E.E"]))   # expected: 1
    print(sol.max_escape(["S#E"]))                 # expected: 0
