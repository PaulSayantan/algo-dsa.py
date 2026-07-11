"""Longest Repeated Substring.

Find the longest substring of `s` that occurs at least twice (overlaps allowed).
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


def longest_repeated_substring(s: str) -> str:
    """Return the longest substring occurring at least twice in `s`.

    Args:
        s: The input string of lowercase English letters.

    Returns:
        The longest repeated substring, or "" if no substring repeats.

    Example:
        >>> longest_repeated_substring("banana")
        'ana'
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(longest_repeated_substring("banana"))       # expected: "ana"
    print(longest_repeated_substring("abcd"))          # expected: ""
    print(longest_repeated_substring("aabcaabdaab"))   # expected: "aab"
