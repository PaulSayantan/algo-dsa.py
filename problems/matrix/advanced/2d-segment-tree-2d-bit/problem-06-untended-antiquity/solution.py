"""
Codeforces 869E - The Untended Antiquity

n x m grid (1-indexed). Operations:
    (1, r1, c1, r2, c2)  -> add a barrier along the boundary of this rectangle
    (2, r1, c1, r2, c2)  -> remove the barrier previously added with these corners
    (3, r1, c1, r2, c2)  -> query: are cells (r1,c1) and (r2,c2) connected
                            without crossing a barrier?  -> "Yes" / "No"

Barriers never intersect or touch, so two cells are connected iff they are
enclosed by exactly the same set of barriers. Assign each barrier a random
64-bit id; "add" range-adds the id to every enclosed cell, "remove" range-
subtracts it. A cell's summed value fingerprints its enclosing set, so a query
compares two point reads.

Implement rectangle-add / point-read with a 2D BIT (range-update / point-query
mode -- see problem 02). Return the answer to every type-3 query, in order.

This is an EMPTY TEMPLATE. Fill in the logic yourself.
"""
import random
from typing import Dict, List, Tuple


class RangeAddPointQueryBIT2D:
    def __init__(self, n: int, m: int) -> None:
        """
        Create a 2D BIT over an n x m, 1-indexed grid supporting rectangle add
        and single-cell read.

        Args:
            n: Number of rows.
            m: Number of columns.

        Returns:
            None.
        """
        # TODO: implement (allocate an (n+2) x (m+2) tree; store n, m)
        pass

    def _add(self, r: int, c: int, delta: int) -> None:
        """
        Internal point-add of `delta` at (r, c) (Fenwick ascent on both axes).

        Args:
            r: 1-indexed row.
            c: 1-indexed column.
            delta: Amount to add at this difference-grid position.

        Returns:
            None.
        """
        # TODO: implement
        pass

    def rect_add(self, r1: int, c1: int, r2: int, c2: int, delta: int) -> None:
        """
        Add `delta` to every cell of the inclusive rectangle [r1..r2] x [c1..c2].

        Args:
            r1, c1: Top-left corner (inclusive, 1-indexed).
            r2, c2: Bottom-right corner (inclusive, 1-indexed).
            delta: Amount to add across the rectangle.

        Returns:
            None.
        """
        # TODO: implement using the four-corner difference stamps:
        #   _add(r1,   c1,   +delta)
        #   _add(r2+1, c1,   -delta)
        #   _add(r1,   c2+1, -delta)
        #   _add(r2+1, c2+1, +delta)
        pass

    def point_value(self, r: int, c: int) -> int:
        """
        Return the accumulated value at cell (r, c) = 2D prefix sum of the
        difference grid up to (r, c).

        Args:
            r: 1-indexed row.
            c: 1-indexed column.

        Returns:
            The current value stored at (r, c).
        """
        # TODO: implement (Fenwick descent on both axes)
        pass


def process(n: int, m: int, operations: List[Tuple[int, int, int, int, int]]) -> List[str]:
    """
    Run all operations and return the "Yes"/"No" answers to type-3 queries.

    Args:
        n: Number of grid rows.
        m: Number of grid columns.
        operations: Each op is (kind, r1, c1, r2, c2) with kind in {1, 2, 3}.

    Returns:
        The list of "Yes"/"No" answers to the type-3 queries, in order.

    Example:
        process(5, 6, [(1,2,2,4,5), (1,3,3,3,3), (3,4,4,1,1),
                       (2,2,2,4,5), (3,1,1,4,4)])
        # -> ["No", "Yes"]
    """
    # TODO: implement
    # Maintain a dict mapping a barrier's corners -> its random 64-bit id.
    #   kind 1: id = random.getrandbits(63)+1; store it; rect_add(..., +id)
    #   kind 2: look up the id; rect_add(..., -id); drop it from the dict
    #   kind 3: answer "Yes" if point_value(r1,c1) == point_value(r2,c2) else "No"
    pass


if __name__ == "__main__":
    ops = [
        (1, 2, 2, 4, 5),
        (1, 3, 3, 3, 3),
        (3, 4, 4, 1, 1),
        (2, 2, 2, 4, 5),
        (3, 1, 1, 4, 4),
    ]
    print(process(5, 6, ops))  # expected: ["No", "Yes"]

    ops2 = [
        (3, 1, 1, 3, 3),
        (1, 2, 2, 2, 2),
        (3, 2, 2, 1, 1),
        (3, 1, 1, 1, 3),
    ]
    print(process(3, 3, ops2))  # expected: ["Yes", "No", "Yes"]
