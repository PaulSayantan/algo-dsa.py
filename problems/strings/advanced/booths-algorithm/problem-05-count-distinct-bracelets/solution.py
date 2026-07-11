"""Count Distinct Bracelets.

A bracelet is a string considered up to rotation AND reflection. Canonicalize
each string to min(least_rotation(s), least_rotation(reverse(s))) using Booth's
Algorithm, then count distinct canonical forms.
"""

from typing import List


def count_distinct_bracelets(words: List[str]) -> int:
    """Return the number of distinct bracelets (strings up to rotation + reflection).

    Two strings are the same bracelet iff one can be turned into the other by some
    combination of rotation and reversal. Strings of different lengths are always
    distinct bracelets.

    Args:
        words: A list of strings.

    Returns:
        The count of distinct bracelets.

    Example:
        >>> count_distinct_bracelets(["abcd", "dcba", "xyyx"])
        2
        >>> count_distinct_bracelets(["abc", "acb"])
        1
    """
    # TODO: implement
    #   canonical(s) = min(smallest_rotation(s), smallest_rotation(s[::-1]))
    #   where smallest_rotation uses Booth's Algorithm.
    #   Count the number of distinct canonical forms.
    pass


if __name__ == "__main__":
    print(count_distinct_bracelets(["abcd", "dcba", "xyyx"]))  # expected: 2
    print(count_distinct_bracelets(["abc", "acb"]))            # expected: 1
    print(count_distinct_bracelets(["ab", "ba", "aab"]))       # expected: 2
