from typing import List, Tuple


def d_query(a: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    """Count distinct values in each queried subarray range.

    Each query ``(l, r)`` (1-indexed, inclusive) asks for the number of distinct
    values among ``a[l..r]``. The array is static and all queries are known in
    advance. Answers are returned in the input order of ``queries``.

    Args:
        a: The 1-indexed array of ``n`` integers, values in ``[1, 10**6]``.
            (Passed as a 0-indexed Python list; treat ``a[0]`` as position 1.)
        queries: A list of ``(l, r)`` pairs with ``1 <= l <= r <= n``.

    Returns:
        A list of integers where the ``t``-th entry is the count of distinct
        values inside ``a[l..r]`` for the ``t``-th query.

    Example:
        >>> d_query([1, 1, 2, 1, 3], [(1, 5), (2, 4), (3, 5)])
        [3, 2, 3]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(
        d_query([1, 1, 2, 1, 3], [(1, 5), (2, 4), (3, 5)])
    )  # expected: [3, 2, 3]
    print(
        d_query([1, 2, 3, 4, 5], [(1, 5), (2, 2), (1, 3)])
    )  # expected: [5, 1, 3]
