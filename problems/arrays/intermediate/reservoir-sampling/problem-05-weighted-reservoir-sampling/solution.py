"""Weighted Reservoir Sampling (Efraimidis-Spirakis, algorithm A-Res).

Fill in `weighted_reservoir_sample` so it returns k items sampled without
replacement with probability proportional to weight, in one pass and O(k) memory.
"""
from typing import Iterable, List, Tuple, TypeVar

T = TypeVar("T")


def weighted_reservoir_sample(stream: Iterable[Tuple[T, float]], k: int) -> List[T]:
    """Return k items sampled by weight from a one-pass stream (A-Res scheme).

    Each item's selection probability is proportional to its positive weight, and
    items are sampled without replacement. For k == 1, item i is returned with
    probability weight_i / (sum of all weights). If the stream yields fewer than k
    items, all of them are returned.

    Args:
        stream: An iterable of (item, weight) pairs of unknown length; consumed
            exactly once. Every weight must be strictly positive.
        k: The desired sample size (k >= 1).

    Returns:
        A list of at most k sampled items (exactly k when the stream has >= k items).

    Example:
        >>> result = weighted_reservoir_sample([("a", 1.0), ("b", 1.0), ("c", 2.0)], 1)
        >>> len(result)
        1
        >>> result[0] in {"a", "b", "c"}
        True
    """
    # TODO: implement A-Res using a size-k min-heap keyed by u ** (1 / weight)
    pass


if __name__ == "__main__":
    print(weighted_reservoir_sample([("a", 1.0), ("b", 1.0), ("c", 2.0)], 1))
    # expected: a single item; "c" is twice as likely as "a" or "b"
    print(weighted_reservoir_sample([("x", 5.0), ("y", 3.0)], 5))
    # expected: ["x", "y"] in some order (fewer than k items)
