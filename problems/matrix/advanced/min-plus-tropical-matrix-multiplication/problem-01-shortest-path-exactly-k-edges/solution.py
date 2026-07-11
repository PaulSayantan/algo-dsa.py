"""Shortest Path with Exactly K Edges.

Empty solution template. Fill in the body yourself.
"""

from typing import List

INF = float("inf")


def shortest_path_k_edges(
    n: int,
    edges: List[List[int]],
    u: int,
    v: int,
    k: int,
) -> int:
    """Return the min total weight of a walk from ``u`` to ``v`` using exactly ``k`` edges.

    Build the weighted adjacency matrix ``W`` (``W[i][j]`` = weight of edge
    ``i -> j``, else ``INF``) and raise it to the ``k``-th power under the
    min-plus / tropical semiring: ``(A ⊙ B)[i][j] = min_t (A[i][t] + B[t][j])``.
    The answer is entry ``(u, v)`` of ``W^{⊙k}`` (return ``-1`` if it is ``INF``).

    Args:
        n: Number of vertices, labeled ``0 .. n-1``.
        edges: List of ``[from, to, weight]`` directed edges.
        u: Source vertex.
        v: Destination vertex.
        k: Exact number of edges the walk must use (``k >= 1``).

    Returns:
        Minimum total weight of a valid exactly-``k``-edge walk, or ``-1`` if
        none exists.

    Example:
        >>> shortest_path_k_edges(
        ...     4, [[0, 1, 2], [0, 2, 1], [1, 3, 3], [2, 1, 1], [2, 3, 5]],
        ...     0, 3, 2)
        5
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    sample_edges = [[0, 1, 2], [0, 2, 1], [1, 3, 3], [2, 1, 1], [2, 3, 5]]
    print(shortest_path_k_edges(4, sample_edges, 0, 3, 2))  # expected: 5
    print(shortest_path_k_edges(4, sample_edges, 0, 3, 3))  # expected: 5
    print(shortest_path_k_edges(4, sample_edges, 0, 3, 1))  # expected: -1
