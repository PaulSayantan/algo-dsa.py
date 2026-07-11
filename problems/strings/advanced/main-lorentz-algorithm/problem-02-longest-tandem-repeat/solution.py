"""Longest Tandem Repeat.

Return the longest square substring (form XX). On ties, return the leftmost.
Return "" if the string is square-free.

Fill in the body yourself. The recommended approach is the Main-Lorentz
algorithm: enumerate all squares as O(n log n) contiguous start-index ranges,
each tagged with its half length l, then take the range with the largest l
(tie-break by smallest start index).
"""

from __future__ import annotations


def longest_tandem_repeat(s: str) -> str:
    """Return the leftmost longest tandem repeat (square ``XX``) in ``s``.

    Args:
        s: The input string (lowercase English letters).

    Returns:
        The longest substring of ``s`` of the form ``XX``. If several are tied for
        the maximum length, the one with the smallest start index. ``""`` if ``s``
        contains no square.

    Example:
        >>> longest_tandem_repeat("banana")
        'anan'
        >>> longest_tandem_repeat("abcde")
        ''
    """
    # TODO: implement using the Main-Lorentz algorithm.
    pass


if __name__ == "__main__":
    print(longest_tandem_repeat("banana"))       # expected: "anan"
    print(longest_tandem_repeat("abcabcabc"))     # expected: "abcabc"
    print(longest_tandem_repeat("abcde"))         # expected: ""
    print(longest_tandem_repeat("aaaa"))          # expected: "aaaa"
