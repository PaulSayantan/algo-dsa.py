from typing import List, Tuple


def powerful_array(a: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    """Compute the ``power`` of each queried subarray range.

    The power of ``a[l..r]`` (1-indexed, inclusive) is
    ``sum over distinct v of (count_v)^2 * v`` where ``count_v`` is the number of
    occurrences of value ``v`` in the range. All queries are known in advance and
    the array is static. Answers are returned in the input order of ``queries``.

    Args:
        a: The 1-indexed array of ``n`` positive integers, values in
            ``[1, 10**6]``. (Passed as a 0-indexed Python list; treat ``a[0]``
            as position 1.)
        queries: A list of ``(l, r)`` pairs with ``1 <= l <= r <= n``.

    Returns:
        A list of integers where the ``t``-th entry is ``power(l, r)`` for the
        ``t``-th query.

    Example:
        >>> powerful_array([1, 2, 1], [(1, 2), (1, 3)])
        [3, 6]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(powerful_array([1, 2, 1], [(1, 2), (1, 3)]))  # expected: [3, 6]
    print(
        powerful_array([1, 1, 2, 2, 1, 3, 1, 1], [(2, 7), (1, 6)])
    )  # expected: [20, 20]
