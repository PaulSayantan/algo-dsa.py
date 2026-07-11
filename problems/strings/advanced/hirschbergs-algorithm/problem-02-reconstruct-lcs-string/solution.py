"""Reconstruct an actual Longest Common Subsequence in O(min(n, m)) space.

Fill in `longest_common_subsequence`. You must return the LCS *string*, not its
length, and you may not build the full (n+1)*(m+1) DP table. Use Hirschberg's
divide-and-conquer: a forward score pass on the top half of `a`, a backward score
pass on the bottom half, then split `b` at the best column and recurse.
"""

from typing import List


def lcs_score_row(a: str, b: str) -> List[int]:
    """Return the last row of the LCS-length DP for `a` vs `b`.

    result[j] = length of the LCS of `a` and `b[:j]`.

    Args:
        a: The string whose characters index the DP rows.
        b: The string whose prefixes index the DP columns.

    Returns:
        A list of length len(b) + 1 of LCS lengths, one rolling row.

    Example:
        >>> lcs_score_row("ab", "ab")
        [0, 1, 2]
    """
    # TODO: implement the single-rolling-row LCS score pass
    pass


def longest_common_subsequence(a: str, b: str) -> str:
    """Return one longest common subsequence of `a` and `b`.

    Args:
        a: First string.
        b: Second string.

    Returns:
        An LCS string of maximum length (any one, if several tie). Empty string
        when the strings share no common subsequence.

    Example:
        >>> longest_common_subsequence("abcde", "ace")
        'ace'
    """
    # TODO: implement Hirschberg's divide-and-conquer reconstruction
    pass


if __name__ == "__main__":
    print(longest_common_subsequence("abcde", "ace"))     # expected: "ace"
    print(longest_common_subsequence("AGGTAB", "GXTXAYB"))  # expected: "GTAB"
    print(longest_common_subsequence("abc", "def"))       # expected: ""
