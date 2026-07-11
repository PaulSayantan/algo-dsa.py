"""Count Distinct Substrings.

Count the number of distinct non-empty substrings of `s`.
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


def count_distinct_substrings(s: str) -> int:
    """Return the number of distinct non-empty substrings of `s`.

    Args:
        s: The input string of lowercase English letters.

    Returns:
        The count of distinct substrings.

    Example:
        >>> count_distinct_substrings("banana")
        15
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(count_distinct_substrings("banana"))  # expected: 15
    print(count_distinct_substrings("aaa"))     # expected: 3
    print(count_distinct_substrings("abc"))     # expected: 6
