"""Longest Substring With At Least K Occurrences.

Find the longest substring of `s` that occurs at least `k` times (overlaps allowed).
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


def longest_substring_at_least_k(s: str, k: int) -> str:
    """Return the longest substring occurring at least `k` times in `s`.

    Args:
        s: The input string of lowercase English letters.
        k: Minimum number of (possibly overlapping) occurrences required.

    Returns:
        The longest qualifying substring, or "" if none exists (k > len(s)).
        Returns the whole string when k <= 1.

    Example:
        >>> longest_substring_at_least_k("banana", 2)
        'ana'
    """
    # TODO: implement
    #  Hint: k occurrences <=> a window of k consecutive suffixes in SA; the
    #  shared prefix length of that window is min(LCP over the window's k-1 gaps).
    #  Maximize that window minimum with a sliding-window-minimum (monotonic deque).
    pass


if __name__ == "__main__":
    print(longest_substring_at_least_k("banana", 2))       # expected: "ana"
    print(longest_substring_at_least_k("banana", 3))       # expected: "a"
    print(longest_substring_at_least_k("mississippi", 2))  # expected: "issi"
