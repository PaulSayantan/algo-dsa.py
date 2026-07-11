"""Build the Suffix Array.

Return the suffix array of a string: the starting indices of all suffixes,
sorted lexicographically. Aim for O(n log n) / O(n log^2 n) via prefix doubling
(or O(n) via DC3/skew), not the naive O(n^2 log n) string sort.
"""
from typing import List


def build_suffix_array(s: str) -> List[int]:
    """Compute the suffix array of ``s``.

    Args:
        s: The input string of length n.

    Returns:
        A list ``sa`` of length n that is a permutation of ``0 .. n-1`` such that
        the suffix ``s[sa[0]:]`` is lexicographically smallest and ``s[sa[n-1]:]``
        is largest.

    Example:
        >>> build_suffix_array("banana")
        [5, 3, 1, 0, 4, 2]
    """
    # TODO: implement (prefix doubling or DC3/skew)
    pass


if __name__ == "__main__":
    print(build_suffix_array("banana"))        # expected: [5, 3, 1, 0, 4, 2]
    print(build_suffix_array("abracadabra"))    # expected: [10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
    print(build_suffix_array("aaaa"))           # expected: [3, 2, 1, 0]
