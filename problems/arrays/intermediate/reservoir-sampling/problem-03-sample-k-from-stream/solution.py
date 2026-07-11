"""Sample K Items From a Stream (Vitter's Algorithm R).

Fill in `reservoir_sample` so it returns a uniform size-k sample drawn without
replacement from a single pass over `stream`, using only O(k) extra memory.
"""
from typing import Iterable, Iterator, List, TypeVar

T = TypeVar("T")


def reservoir_sample(stream: Iterable[T], k: int) -> List[T]:
    """Return a uniform random sample of size k from a one-pass stream.

    Every item in the stream must end up in the returned list with probability
    exactly k / n, where n is the (unknown-in-advance) number of items. If the
    stream yields fewer than k items, all of them are returned.

    Args:
        stream: An iterable/iterator of items of unknown length. It is consumed
            exactly once, front to back.
        k: The desired sample size (k >= 1).

    Returns:
        A list of at most k sampled items (exactly k when the stream has >= k items).

    Example:
        >>> result = reservoir_sample([10, 20, 30, 40, 50], 2)
        >>> len(result)
        2
        >>> all(x in {10, 20, 30, 40, 50} for x in result)
        True
    """
    # TODO: implement Reservoir Sampling (Algorithm R) with a reservoir of size k
    pass


if __name__ == "__main__":
    print(reservoir_sample([10, 20, 30, 40, 50], 2))  # expected: 2 distinct items from the stream
    print(reservoir_sample([7, 8], 5))                # expected: [7, 8] (fewer than k items)
