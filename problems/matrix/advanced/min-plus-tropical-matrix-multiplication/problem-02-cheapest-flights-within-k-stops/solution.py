"""LeetCode 787 — Cheapest Flights Within K Stops.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        """Return the cheapest price from ``src`` to ``dst`` using at most ``k`` stops.

        Model the flights as a cost matrix ``M`` with ``0`` on the diagonal
        (a free "stay put" self-loop) so that "at most" becomes "exactly". Under
        the min-plus / tropical semiring
        ``(A ⊙ B)[i][j] = min_t (A[i][t] + B[t][j])``, the ``(k+1)``-th tropical
        power of ``M`` gives, in entry ``(src, dst)``, the cheapest route using
        at most ``k + 1`` flights (= at most ``k`` stops). Return ``-1`` if it is
        infinite.

        Args:
            n: Number of cities, labeled ``0 .. n-1``.
            flights: List of ``[from, to, price]`` directed flights.
            src: Start city.
            dst: Destination city.
            k: Maximum number of intermediate stops allowed.

        Returns:
            Cheapest total price using at most ``k`` stops, or ``-1`` if
            unreachable within the limit.

        Example:
            >>> Solution().findCheapestPrice(
            ...     4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
            ...     0, 3, 1)
            700
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findCheapestPrice(
        4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
        0, 3, 1))  # expected: 700
    print(sol.findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))  # expected: 200
    print(sol.findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))  # expected: 500
