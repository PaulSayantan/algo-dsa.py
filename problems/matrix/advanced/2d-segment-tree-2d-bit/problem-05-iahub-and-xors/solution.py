"""
Codeforces 341D - Iahub and Xors

n x n matrix (1-indexed), initially zeros. Operations:
    (1, x0, y0, x1, y1)      -> query: XOR of the submatrix, return it
    (2, x0, y0, x1, y1, v)   -> update: a[i][j] ^= v over the submatrix

Return the answer to every query, in order.

Idea: 2D BIT in RANGE-UPDATE / RANGE-QUERY mode specialized for XOR. The sum
version needs four BITs indexed by coordinate parity; for XOR the same four
parity buckets ((x & 1), (y & 1)) suffice because XORing a value an even number
of times cancels, so only the parity of how many times a cell is included
matters.

This is an EMPTY TEMPLATE. Fill in the logic yourself.
"""
from typing import List, Tuple, Union

Operation = Union[Tuple[int, int, int, int, int],
                  Tuple[int, int, int, int, int, int]]


class XorBIT2D:
    def __init__(self, n: int) -> None:
        """
        Create the structure over an n x n, 1-indexed, all-zero matrix.

        Args:
            n: Side length of the square matrix.

        Returns:
            None.
        """
        # TODO: implement
        # Maintain 4 BITs (or one BIT indexed by parity buckets), each of size
        # (n+1) x (n+1), where bucket = (x & 1) * 2 + (y & 1).
        pass

    def _point_xor(self, x: int, y: int, v: int) -> None:
        """
        Internal: XOR v into the parity bucket for (x, y) and propagate.

        Args:
            x: 1-indexed row of the difference stamp.
            y: 1-indexed column of the difference stamp.
            v: Value to fold in with XOR.

        Returns:
            None.
        """
        # TODO: implement (Fenwick ascent on both axes into bucket (x&1, y&1))
        pass

    def _prefix_xor(self, x: int, y: int) -> int:
        """
        Internal: XOR of a[i][j] over the prefix rectangle [1..x] x [1..y].

        Args:
            x: 1-indexed row upper bound of the prefix.
            y: 1-indexed column upper bound of the prefix.

        Returns:
            The XOR over the prefix rectangle.
        """
        # TODO: implement
        # Reconstruct using the parity of x and y: pick the bucket by (x&1,y&1)
        # while descending both Fenwick axes, XOR-accumulating contributions.
        pass

    def update(self, x0: int, y0: int, x1: int, y1: int, v: int) -> None:
        """
        XOR v into every cell of the inclusive submatrix [x0..x1] x [y0..y1].

        Args:
            x0, y0: Top-left corner (inclusive, 1-indexed).
            x1, y1: Bottom-right corner (inclusive, 1-indexed).
            v: Value to XOR into each cell.

        Returns:
            None.
        """
        # TODO: implement
        # Four-corner difference stamps, XOR analogue of the sum version:
        #   _point_xor(x0,   y0,   v)
        #   _point_xor(x1+1, y0,   v)
        #   _point_xor(x0,   y1+1, v)
        #   _point_xor(x1+1, y1+1, v)
        pass

    def query(self, x0: int, y0: int, x1: int, y1: int) -> int:
        """
        Return the XOR over the inclusive submatrix [x0..x1] x [y0..y1].

        Args:
            x0, y0: Top-left corner (inclusive, 1-indexed).
            x1, y1: Bottom-right corner (inclusive, 1-indexed).

        Returns:
            The XOR of all cells in the submatrix.
        """
        # TODO: implement
        # Inclusion-exclusion, but with XOR the signs vanish:
        #   P(x1,y1) ^ P(x0-1,y1) ^ P(x1,y0-1) ^ P(x0-1,y0-1)
        pass


def process(n: int, operations: List[Operation]) -> List[int]:
    """
    Run every operation and return the list of query answers.

    Args:
        n: Side length of the square matrix.
        operations: Each op is (1, x0, y0, x1, y1) for a query or
            (2, x0, y0, x1, y1, v) for an update. All coordinates 1-indexed.

    Returns:
        The answers to the type-1 (query) operations, in order.

    Example:
        process(3, [(2,1,1,2,2,1),(2,1,3,2,3,2),(2,3,1,3,3,3),
                    (1,2,2,3,3),(1,2,2,3,2)])
        # -> [3, 2]
    """
    # TODO: implement (build XorBIT2D(n); dispatch update/query)
    pass


if __name__ == "__main__":
    ops = [
        (2, 1, 1, 2, 2, 1),
        (2, 1, 3, 2, 3, 2),
        (2, 3, 1, 3, 3, 3),
        (1, 2, 2, 3, 3),
        (1, 2, 2, 3, 2),
    ]
    print(process(3, ops))  # expected: [3, 2]

    ops2 = [
        (2, 1, 1, 2, 2, 5),
        (1, 1, 1, 2, 2),
        (1, 1, 1, 1, 1),
    ]
    print(process(2, ops2))  # expected: [0, 5]
