"""Tree and Queries (Codeforces 375D) — empty solution template.

Fill in the body using an Euler-tour flatten plus Mo's algorithm (offline sqrt
decomposition on queries). Do NOT change the function signature.
"""
from typing import List, Tuple


def tree_and_queries(
    n: int,
    colors: List[int],
    edges: List[Tuple[int, int]],
    queries: List[Tuple[int, int]],
) -> List[int]:
    """Answer subtree color-frequency queries.

    For each query (v, k), count how many colors occur at least k times among
    the vertices of the subtree rooted at v.

    Args:
        n: Number of vertices, labeled 1..n; the tree is rooted at vertex 1.
        colors: Length-n list where colors[i] is the color of vertex (i + 1).
        edges: The n - 1 undirected edges as (u, v) vertex pairs (1-indexed).
        queries: A list of (v, k) pairs: vertex v (1-indexed) and threshold k.

    Returns:
        A list of integers, one per query in the ORIGINAL query order; the i-th
        entry is the number of colors appearing >= k times in subtree(v).

    Example:
        >>> tree_and_queries(4, [1, 2, 3, 2],
        ...                  [(1, 2), (1, 3), (2, 4)],
        ...                  [(1, 1), (1, 2), (2, 1), (3, 1)])
        [3, 1, 1, 1]
    """
    # TODO: implement:
    #   1. Build adjacency list; run an iterative DFS from vertex 1 to compute
    #      tin[v], tout[v], and a flat[] array of colors in entry-time order.
    #   2. Map query (v, k) to range [tin[v], tout[v]] on flat[], remembering k.
    #   3. Run Mo's algorithm over flat[]. Maintain cnt[color] and
    #      atLeast[t] = number of colors with current count >= t.
    #        add: cnt[c] += 1; atLeast[cnt[c]] += 1
    #        remove: atLeast[cnt[c]] -= 1; cnt[c] -= 1
    #   4. For each query answer atLeast[k] (0 if k > subtree size).
    pass


if __name__ == "__main__":
    sample_n = 4
    sample_colors = [1, 2, 3, 2]
    sample_edges = [(1, 2), (1, 3), (2, 4)]
    sample_queries = [(1, 1), (1, 2), (2, 1), (3, 1)]
    print(tree_and_queries(sample_n, sample_colors, sample_edges, sample_queries))
    # Expected: [3, 1, 1, 1]
