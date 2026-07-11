"""Longest Repeated Substring.

Find the longest substring that appears at least twice in S (overlaps allowed).
Build the suffix array, compute the LCP array (Kasai), and take the shared prefix
at the position of the maximum LCP value.
"""
from typing import List


def longest_repeated_substring(s: str) -> str:
    """Return a longest substring of ``s`` that occurs at least twice.

    Args:
        s: The input string.

    Returns:
        A longest repeated substring (overlapping occurrences allowed). If no
        substring repeats, returns the empty string "". If several are tied for
        the maximum length, any one of them is acceptable.

    Example:
        >>> longest_repeated_substring("banana")
        'ana'
    """
    # TODO: build suffix array, build LCP array (Kasai), find index of max LCP,
    # and return s[sa[i] : sa[i] + lcp[i]].
    pass


if __name__ == "__main__":
    print(longest_repeated_substring("banana"))          # expected: "ana"
    print(longest_repeated_substring("abcpqrabcxyz"))      # expected: "abc"
    print(longest_repeated_substring("abcd"))              # expected: ""
