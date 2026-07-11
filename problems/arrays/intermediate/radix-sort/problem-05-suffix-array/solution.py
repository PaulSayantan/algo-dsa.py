from typing import List


def build_suffix_array(s: str) -> List[int]:
    """Build the suffix array of ``s`` using prefix doubling + radix sort.

    Returns the starting indices of all suffixes of ``s`` in ascending
    lexicographic order. The intended method:
      1. Rank suffixes by their first character.
      2. Repeatedly double the compared prefix length: represent each suffix by
         the pair ``(rank[i], rank[i + len])`` and stably radix-sort those pairs
         (sort by the second key, then by the first).
      3. Recompute ranks after each round; stop once all ranks are distinct.

    Args:
        s: A non-empty lowercase string of length ``n``.

    Returns:
        A list of ``n`` integers: a permutation of ``0..n-1`` giving suffix start
        indices in sorted order.

    Example:
        >>> build_suffix_array("banana")
        [5, 3, 1, 0, 4, 2]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(build_suffix_array("banana"))
    # Expected: [5, 3, 1, 0, 4, 2]
    print(build_suffix_array("abab"))
    # Expected: [2, 0, 3, 1]
    print(build_suffix_array("aaa"))
    # Expected: [2, 1, 0]
