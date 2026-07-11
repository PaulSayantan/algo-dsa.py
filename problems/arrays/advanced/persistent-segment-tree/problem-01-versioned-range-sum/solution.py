"""Versioned Range Sum (Time-Travel Array).

Implement a fully persistent array supporting point updates that fork new
versions and range-sum queries against any historical version.

Fill in the body of `process_operations`. Do NOT mutate previous versions.
"""

from typing import List, Tuple, Union

# An operation is one of:
#   ("update", prev_version, index, value)
#   ("query",  version, l, r)
Operation = Tuple[Union[str, int], ...]


def process_operations(
    n: int,
    initial: List[int],
    operations: List[Operation],
) -> List[int]:
    """Process versioned update/query operations on a persistent array.

    Version 0 is ``initial``. Each ``("update", prev_version, index, value)``
    creates a brand-new version (ids assigned 1, 2, 3, ... in creation order)
    that equals ``prev_version`` with ``index`` set to ``value``; the base
    version is left unchanged. Each ``("query", version, l, r)`` asks for the
    inclusive sum of positions ``l..r`` as they looked in ``version``.

    Args:
        n: Length of the array.
        initial: The version-0 contents, length ``n``.
        operations: The list of update/query operations to process in order.

    Returns:
        A list with one integer per ``query`` operation, in query order.

    Example:
        >>> process_operations(
        ...     5,
        ...     [1, 2, 3, 4, 5],
        ...     [("query", 0, 0, 4),
        ...      ("update", 0, 2, 10),
        ...      ("query", 1, 0, 4),
        ...      ("query", 0, 0, 4)],
        ... )
        [15, 22, 15]
    """
    # TODO: implement using a persistent segment tree (one root per version)
    pass


if __name__ == "__main__":
    # Expected output: [15, 22, 15]
    print(
        process_operations(
            5,
            [1, 2, 3, 4, 5],
            [
                ("query", 0, 0, 4),
                ("update", 0, 2, 10),
                ("query", 1, 0, 4),
                ("query", 0, 0, 4),
            ],
        )
    )

    # Expected output: [15, 6, 10]
    print(
        process_operations(
            3,
            [5, 5, 5],
            [
                ("update", 0, 0, 1),
                ("update", 1, 2, 9),
                ("query", 2, 0, 2),
                ("query", 1, 0, 1),
                ("query", 0, 1, 2),
            ],
        )
    )
