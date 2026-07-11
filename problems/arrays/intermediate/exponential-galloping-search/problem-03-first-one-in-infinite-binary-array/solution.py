"""First 1 in an Infinite Sorted Binary Array (classic interview problem).

Fill in `first_one` using the Exponential (Galloping) Search technique on the
monotonic predicate "is bits[i] == 1?". The array is conceptually infinite:
0s followed by 1s forever, so a first 1 always exists. Reads go through
reader.get(i) for any i >= 0.
"""


class BitReader:
    """Read-only view over an infinite sorted 0/1 array (0s then 1s forever).

    get(i) returns bits[i] for any index i >= 0. Provided by the judge; a
    reference implementation is included here only so the __main__ block can run
    locally. A finite prefix is supplied and the infinite tail is all 1s.
    """

    def __init__(self, prefix):
        self._prefix = prefix

    def get(self, index: int) -> int:
        if index < len(self._prefix):
            return self._prefix[index]
        return 1  # the infinite tail is all 1s


def first_one(reader: "BitReader") -> int:
    """Return the index of the first 1 in an infinite sorted 0/1 array.

    Args:
        reader: A BitReader over an infinite array of 0s followed by 1s. Reads
            past the end conceptually fall into the all-1s tail, so a first 1
            always exists.

    Returns:
        The smallest index `t` with `reader.get(t) == 1`.

    Example:
        >>> first_one(BitReader([0, 0, 0, 0, 1, 1, 1]))
        4
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    # The list is the finite prefix; index >= len(prefix) reads as 1 (the tail).
    print(first_one(BitReader([0, 0, 0, 0, 1, 1, 1])))                 # expected: 4
    print(first_one(BitReader([1, 1, 1, 1])))                          # expected: 0
    print(first_one(BitReader([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])))        # expected: 9
