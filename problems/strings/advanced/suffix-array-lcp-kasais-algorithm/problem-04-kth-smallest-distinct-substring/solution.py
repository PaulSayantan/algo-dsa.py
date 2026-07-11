"""K-th Smallest Distinct Substring.

Return the k-th lexicographically smallest distinct substring of `s`.
"""
from typing import List


def build_suffix_array(s: str) -> List[int]:
    """Return the suffix array of `s` (sorted starting indices of all suffixes).

    Args:
        s: The input string.

    Returns:
        A list SA where SA[i] is the start index of the i-th smallest suffix.
    """
    # TODO: implement (e.g. prefix-doubling in O(n log n))
    pass


def build_lcp_kasai(s: str, sa: List[int]) -> List[int]:
    """Return the LCP array for `s` given its suffix array, using Kasai's algorithm.

    Args:
        s: The input string.
        sa: The suffix array of `s`.

    Returns:
        A list LCP where LCP[i] is the longest common prefix length of the
        suffixes SA[i-1] and SA[i]; LCP[0] is 0.
    """
    # TODO: implement Kasai's O(n) LCP construction
    pass


def kth_smallest_distinct_substring(s: str, k: int) -> str:
    """Return the k-th lexicographically smallest distinct substring of `s`.

    Args:
        s: The input string of lowercase English letters.
        k: 1-indexed rank of the desired distinct substring.

    Returns:
        The k-th smallest distinct substring, or "-1" if k exceeds the number of
        distinct substrings.

    Example:
        >>> kth_smallest_distinct_substring("dbac", 3)
        'b'
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(kth_smallest_distinct_substring("dbac", 3))    # expected: "b"
    print(kth_smallest_distinct_substring("dbac", 5))    # expected: "bac"
    print(kth_smallest_distinct_substring("banana", 6))  # expected: "b"
