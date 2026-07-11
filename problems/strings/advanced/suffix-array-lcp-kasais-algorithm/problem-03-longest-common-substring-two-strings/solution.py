"""Longest Common Substring of Two Strings.

Find the longest contiguous substring shared by strings `a` and `b`.
"""
from typing import List


def build_suffix_array(s: str) -> List[int]:
    """Return the suffix array of `s` (sorted starting indices of all suffixes).

    Args:
        s: The input string (may include separator characters).

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


def longest_common_substring(a: str, b: str) -> str:
    """Return the longest contiguous substring common to `a` and `b`.

    Args:
        a: The first string of lowercase English letters.
        b: The second string of lowercase English letters.

    Returns:
        The longest common substring, or "" if none exists.

    Example:
        >>> longest_common_substring("abcde", "cdefg")
        'cde'
    """
    # TODO: implement
    #  Hint: work over s = a + '#' + b + '$'; an adjacent sorted-suffix pair
    #  qualifies when one suffix starts inside `a` and the other inside `b`.
    pass


if __name__ == "__main__":
    print(longest_common_substring("abcde", "cdefg"))              # expected: "cde"
    print(longest_common_substring("GeeksforGeeks", "GeeksQuiz"))  # expected: "Geeks"
    print(longest_common_substring("abc", "xyz"))                  # expected: ""
