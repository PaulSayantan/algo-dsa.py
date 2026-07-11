"""Min-Cost Walk of Exactly K Edges (Huge K).

Empty solution template. Fill in the body yourself.
"""

from typing import List

INF = float("inf")


def min_cost_walk_k_edges(
    n: int,
    W: List[List[float]],
    u: int,
    v: int,
    k: int,
) -> int:
    """Return the min weight of a walk from ``u`` to ``v`` using exactly ``k`` edges.

    ``k`` can be as large as ``10**18``, so a linear chain of ``k`` products is
    infeasible. Use fast (binary) exponentiation of ``W`` under the min-plus /
    tropical semiring: ``(A ⊙ B)[i][j] = min_t (A[i][t] + B[t][j])``, starting
    from the tropical identity (``0`` on the diagonal, ``INF`` elsewhere). The
    answer is entry ``(u, v)`` of ``W^{⊙k}``, or ``-1`` if it is ``INF``.

    Args:
        n: Number of vertices, labeled ``0 .. n-1``.
        W: ``n x n`` weight matrix; ``W[i][j]`` is the cost of edge ``i -> j`` or
            ``INF`` if absent.
        u: Source vertex.
        v: Destination vertex.
        k: Exact number of edges (``1 <= k <= 10**18``).

    Returns:
        Minimum total weight of an exactly-``k``-edge walk, or ``-1`` if none
        exists.

    Example:
        >>> min_cost_walk_k_edges(2, [[5, 2], [3, 1]], 0, 0, 4)
        7
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    W = [[5, 2], [3, 1]]
    print(min_cost_walk_k_edges(2, W, 0, 0, 4))   # expected: 7
    print(min_cost_walk_k_edges(2, W, 1, 1, 10))  # expected: 10
    print(min_cost_walk_k_edges(2, W, 0, 1, 4))   # expected: 5
