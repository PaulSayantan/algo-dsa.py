"""Count walks of length exactly k between two nodes, modulo 1e9+7.

Fill in the body using Matrix Exponentiation on the adjacency matrix.
k can be as large as 10**18, so step-by-step DP is too slow.
"""

from typing import List

MOD = 10**9 + 7


def count_walks(adj: List[List[int]], src: int, dst: int, k: int) -> int:
    """Return the number of walks of length exactly k from src to dst.

    A walk of length k is a sequence of k edges u_0 -> u_1 -> ... -> u_k with
    u_0 = src and u_k = dst; nodes and edges may repeat.

    Args:
        adj: V x V adjacency matrix; adj[i][j] == 1 iff edge i -> j exists.
        src: Source node index (0-based).
        dst: Destination node index (0-based).
        k:   Required walk length (number of edges), 1 <= k <= 10**18.

    Returns:
        The count of length-k walks from src to dst, modulo 10**9 + 7.

    Example:
        >>> count_walks([[0,1,1],[1,0,1],[1,1,0]], 0, 0, 2)
        2
    """
    # TODO: implement by raising the adjacency matrix to the k-th power
    #       (fast exponentiation) and reading entry [src][dst].
    pass


if __name__ == "__main__":
    triangle = [[0, 1, 1],
                [1, 0, 1],
                [1, 1, 0]]
    print(count_walks(triangle, 0, 0, 2))  # expected: 2
    print(count_walks(triangle, 0, 1, 3))  # expected: 3
