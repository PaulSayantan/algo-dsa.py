"""Count Distinct Values on Tree Paths (SPOJ COT2) — Mo's Algorithm on a tree.

For each offline query (u, v), count the distinct node-values on the simple path
between u and v.

Approach: Euler-flatten the tree (entry time st[node], exit time en[node]) so the
path maps to a contiguous range of the Euler array, then run Mo's Algorithm with a
"toggle" add/remove (a node seen an even number of times in the window is absent).
Use LCA to combine the two branches; add the LCA's value separately when it is not an
endpoint. Total time O((n + q) * sqrt(n)).

Fill in the function body. Do NOT walk each path explicitly per query
(that is the O(q * n) brute force).
"""
from typing import List, Tuple


def tree_path_distinct(
    n: int,
    edges: List[Tuple[int, int]],
    vals: List[int],
    queries: List[Tuple[int, int]],
) -> List[int]:
    """Count distinct values on each queried tree path.

    Args:
        n: Number of nodes, labeled 0 .. n-1.
        edges: The n-1 undirected tree edges as (u, v) pairs, 0-indexed.
        vals: vals[i] is the value stored at node i (0-indexed).
        queries: A list of (u, v) node pairs (0-indexed); count distinct values on
            the simple path from u to v, inclusive of both endpoints.

    Returns:
        A list `ans` where ans[k] is the number of distinct values on the path for
        the k-th query, in original query order.

    Example:
        # Tree (0-indexed): 0-1, 0-2, 1-3, 1-4 ; vals = [1, 2, 1, 3, 2]
        tree_path_distinct(5, [(0,1),(0,2),(1,3),(1,4)], [1,2,1,3,2],
                           [(3,4), (3,2)])
        # -> [2, 3]
    """
    # TODO: implement using Euler tour + LCA + Mo's Algorithm
    pass


if __name__ == "__main__":
    # Same tree as PROBLEM.md, converted to 0-indexed:
    #   nodes 1..5 -> 0..4 ; vals {1:1,2:2,3:1,4:3,5:2} -> [1,2,1,3,2]
    #   edges 1-2,1-3,2-4,2-5 -> (0,1),(0,2),(1,3),(1,4)
    edges = [(0, 1), (0, 2), (1, 3), (1, 4)]
    vals = [1, 2, 1, 3, 2]
    print(tree_path_distinct(5, edges, vals, [(3, 4), (3, 2)]))  # expected: [2, 3]
    print(tree_path_distinct(5, edges, vals, [(0, 0), (1, 3)]))  # expected: [1, 2]
