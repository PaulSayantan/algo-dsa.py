"""Traveling Salesman — Minimum Cost Tour via Held-Karp.

Find the cheapest Hamiltonian cycle that starts and ends at city 0.

Solve this with Bitmask DP (Held-Karp): let `dp[mask][last]` be the minimum
cost of a path that starts at city 0, visits exactly the cities in `mask`, and
currently stands at city `last` (where bit `last` is set in `mask`). Close the
tour by adding the return edge to city 0.
"""

from __future__ import annotations

from typing import List


def tsp_min_cost(dist: List[List[int]]) -> int:
    """Return the minimum cost of a round trip visiting every city once.

    Args:
        dist: An n x n matrix where dist[i][j] is the travel cost from city i
            to city j. dist[i][i] == 0. 1 <= n <= 15.

    Returns:
        The minimum total cost of a tour that starts at city 0, visits all
        other cities exactly once, and returns to city 0. Returns 0 when
        there is a single city.

    Example:
        >>> tsp_min_cost([[0, 10, 15, 20],
        ...               [10, 0, 35, 25],
        ...               [15, 35, 0, 30],
        ...               [20, 25, 30, 0]])
        80
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    m = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    print(tsp_min_cost(m))                       # expected: 80
    print(tsp_min_cost([[0, 1, 1], [1, 0, 1], [1, 1, 0]]))  # expected: 3
    print(tsp_min_cost([[0]]))                   # expected: 0
