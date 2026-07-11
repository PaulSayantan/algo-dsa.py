"""USACO Cow Relays — shortest path using exactly N edges.

Empty solution template. Fill in the body yourself.
"""

from typing import List, Tuple

INF = float("inf")


def cow_relays(
    n_edges_required: int,
    edges: List[Tuple[int, int, int]],
    start: int,
    end: int,
) -> int:
    """Return the shortest ``start -> end`` path using exactly ``n_edges_required`` edges.

    The graph is undirected with sparse vertex labels. Compress the distinct
    endpoints to contiguous indices, build the ``m x m`` symmetric weight matrix
    ``W`` (``W[a][b] = W[b][a] = w``), and raise it to the
    ``n_edges_required``-th power under the min-plus / tropical semiring
    ``(A ⊙ B)[i][j] = min_t (A[i][t] + B[t][j])`` using fast exponentiation
    (``N`` can be up to ``10**6``). The answer is entry ``(start, end)`` of that
    tropical power.

    Args:
        n_edges_required: Exact number of edges the path must use (``N``).
        edges: List of ``(weight, endpoint_u, endpoint_v)`` undirected edges.
        start: Start vertex label ``S``.
        end: End vertex label ``E``.

    Returns:
        Length of the shortest exactly-``N``-edge path from ``start`` to ``end``.

    Example:
        >>> cow_relays(2, [(11,4,6),(4,4,8),(8,4,9),(6,6,8),(2,6,9),(3,8,9)], 6, 4)
        10
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    sample_edges = [(11, 4, 6), (4, 4, 8), (8, 4, 9),
                    (6, 6, 8), (2, 6, 9), (3, 8, 9)]
    print(cow_relays(2, sample_edges, 6, 4))  # expected: 10
    print(cow_relays(4, sample_edges, 6, 4))  # expected: 14
