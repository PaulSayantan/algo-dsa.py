from typing import List, Tuple


def k_query(a: List[int], queries: List[Tuple[int, int, int]]) -> List[int]:
    """Count, for each query, elements greater than ``k`` in a subarray range.

    Each query ``(i, j, k)`` (1-indexed, inclusive) asks how many positions
    ``p`` with ``i <= p <= j`` have ``a[p] > k``. The array is never modified,
    and every query is known in advance. Answers are returned in the input
    order of ``queries``.

    Args:
        a: The 1-indexed array of ``n`` integers, values in ``[1, 10**9]``.
            (Passed as a 0-indexed Python list; treat ``a[0]`` as position 1.)
        queries: A list of ``(i, j, k)`` triples with ``1 <= i <= j <= n`` and
            ``1 <= k <= 10**9``.

    Returns:
        A list of integers where the ``t``-th entry is the count of elements
        ``> k`` inside ``a[i..j]`` for the ``t``-th query.

    Example:
        >>> k_query([5, 1, 2, 3, 4], [(2, 4, 1), (4, 4, 4), (1, 5, 2)])
        [2, 0, 3]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(
        k_query([5, 1, 2, 3, 4], [(2, 4, 1), (4, 4, 4), (1, 5, 2)])
    )  # expected: [2, 0, 3]
    print(
        k_query(
            [1, 2, 3, 4, 5, 6, 7], [(1, 7, 0), (1, 7, 7), (3, 5, 3)]
        )
    )  # expected: [7, 0, 2]
