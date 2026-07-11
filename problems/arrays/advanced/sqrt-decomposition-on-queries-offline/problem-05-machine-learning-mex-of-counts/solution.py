"""Machine Learning / Mex of Occurrence Counts (Codeforces 940F) —
empty solution template.

Fill in the body using Mo's algorithm WITH point updates (3D Mo's / Mo's with
modifications). Do NOT change the function signature.
"""
from typing import List, Tuple


def mex_of_counts(
    n: int,
    a: List[int],
    ops: List[Tuple[int, int, int]],
) -> List[int]:
    """Process interleaved subarray-mex queries and point updates.

    Each op is a 3-tuple:
      * (1, l, r): output the mex of the multiset of occurrence counts of the
        distinct values in a[l..r] (1-indexed inclusive). "mex" here is the
        smallest POSITIVE integer that is not an occurrence count of any value.
      * (2, p, x): set a[p] = x (1-indexed position); affects later ops.

    Args:
        n: Length of the array.
        a: The initial array (length n, values 1..1e9). 1-indexed in the problem;
            index internally as you prefer.
        ops: The list of operations in the given order.

    Returns:
        A list with one integer per type-1 query, in the order those queries
        appear in `ops`.

    Example:
        >>> mex_of_counts(6, [1, 2, 3, 3, 3, 2],
        ...               [(1, 1, 3), (2, 2, 3), (1, 1, 3)])
        [2, 3]
    """
    # TODO: implement Mo's with updates:
    #   1. Coordinate-compress all values (initial array + update values).
    #   2. Separate ops into type-1 queries (l, r, time) and type-2 updates
    #      (pos, new_val, old_val). `time` = number of updates seen before it.
    #   3. Block size ~ n^(2/3). Sort queries by (l // B, r // B, time).
    #   4. Maintain cnt[value] and occ[t] = number of values occurring t times.
    #      add/remove adjust both; a point update is "undo old value if in
    #      window, apply new value if in window" while rolling `time` forward or
    #      backward.
    #   5. Answer a type-1 query by scanning t = 1, 2, ... until occ[t] == 0.
    pass


if __name__ == "__main__":
    sample_n = 6
    sample_a = [1, 2, 3, 3, 3, 2]
    sample_ops = [(1, 1, 3), (2, 2, 3), (1, 1, 3)]
    print(mex_of_counts(sample_n, sample_a, sample_ops))
    # Expected: [2, 3]
