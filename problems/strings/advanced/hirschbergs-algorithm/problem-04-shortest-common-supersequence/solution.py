"""Shortest Common Supersequence, with the LCS found in O(min(n, m)) space.

Fill in `shortest_common_supersequence`. Recover a longest common subsequence with
Hirschberg's divide-and-conquer (linear space), then interleave str1 and str2 along
that LCS: write each private run of characters in order, and write each shared LCS
character exactly once.
"""

from typing import List


def lcs_score_row(a: str, b: str) -> List[int]:
    """Return the last row of the LCS-length DP for `a` vs `b`.

    result[j] = length of the LCS of `a` and `b[:j]`.

    Args:
        a: String indexing the DP rows.
        b: String indexing the DP columns.

    Returns:
        A list of length len(b) + 1, one rolling row of LCS lengths.
    """
    # TODO: implement the single-rolling-row LCS score pass
    pass


def hirschberg_lcs(a: str, b: str) -> str:
    """Return one longest common subsequence of `a` and `b` in O(min) space.

    Args:
        a: First string.
        b: Second string.

    Returns:
        An LCS string (any one of maximum length); "" if none.
    """
    # TODO: implement Hirschberg's divide-and-conquer LCS reconstruction
    pass


def shortest_common_supersequence(str1: str, str2: str) -> str:
    """Return a shortest string having both str1 and str2 as subsequences.

    Args:
        str1: First string.
        str2: Second string.

    Returns:
        A shortest common supersequence (any one, if several tie).

    Example:
        >>> shortest_common_supersequence("abac", "cab")
        'cabac'
    """
    # TODO: recover the LCS with Hirschberg, then interleave str1 and str2 along it
    pass


if __name__ == "__main__":
    print(shortest_common_supersequence("abac", "cab"))  # expected len 5, e.g. "cabac"
    print(shortest_common_supersequence("geek", "eke"))  # expected len 5, e.g. "geeke"
    print(shortest_common_supersequence("abc", "def"))   # expected len 6, e.g. "abcdef"
