"""
Count Points in a Rectangle (online 2D range-counting).

Support a stream of operations:
    ("add", x, y)                  -> insert a point at (x, y)
    ("count", x1, y1, x2, y2)      -> how many inserted points lie in the
                                      inclusive rectangle [x1,x2] x [y1,y2]

Return the answer to every "count" operation, in order.

Idea: keep a 2D BIT of point frequencies; answer each rectangle by
inclusion-exclusion of four prefix counts. Coordinates are up to 1e9, so
compress them first (the operation list is fully available, so gather every
coordinate that can appear as an index and map it to a small rank).

This is an EMPTY TEMPLATE. Fill in the logic yourself.
"""
from typing import List, Tuple, Union

Operation = Union[Tuple[str, int, int], Tuple[str, int, int, int, int]]


def count_points_in_rectangles(operations: List[Operation]) -> List[int]:
    """
    Process the operation stream and return every 'count' answer in order.

    Args:
        operations: A list where each element is either
            ("add", x, y) to insert a point, or
            ("count", x1, y1, x2, y2) to query a rectangle (inclusive).

    Returns:
        A list of integers: one answer per "count" operation, in the order the
        count operations appeared.

    Example:
        ops = [("add", 1, 1), ("add", 4, 4), ("add", 2, 3),
               ("count", 1, 1, 4, 4), ("count", 3, 1, 4, 4),
               ("count", 5, 5, 9, 9)]
        count_points_in_rectangles(ops)  # -> [3, 1, 0]
    """
    # TODO: implement
    # Outline:
    #   1. Coordinate-compress x and y:
    #        - collect every x/y that could be used as a BIT index
    #          (add points contribute x,y; count bounds x1,x2,y1,y2 are only
    #           used for lookups, so binary-search them into the compressed
    #           arrays with the right rounding).
    #   2. Build a 2D BIT sized (len(xs)+1) x (len(ys)+1) of frequencies.
    #   3. "add": point-add +1 at the compressed (rank_x, rank_y).
    #   4. "count": prefix(x2,y2) - prefix(x1-1,y2) - prefix(x2,y1-1)
    #                 + prefix(x1-1,y1-1), where each bound is mapped to a
    #                 compressed prefix boundary (upper_bound for x2/y2,
    #                 lower_bound-1 for x1-1/y1-1).
    pass


if __name__ == "__main__":
    ops = [
        ("add", 1, 1),
        ("add", 4, 4),
        ("add", 2, 3),
        ("count", 1, 1, 4, 4),
        ("count", 3, 1, 4, 4),
        ("count", 5, 5, 9, 9),
    ]
    print(count_points_in_rectangles(ops))  # expected: [3, 1, 0]

    ops2 = [
        ("add", 2, 2),
        ("add", 2, 2),
        ("count", 2, 2, 2, 2),
        ("count", 1, 1, 3, 3),
        ("count", 3, 3, 5, 5),
    ]
    print(count_points_in_rectangles(ops2))  # expected: [2, 2, 0]
