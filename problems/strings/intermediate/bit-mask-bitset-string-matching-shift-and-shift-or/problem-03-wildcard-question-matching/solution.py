"""Wildcard '?' substring search using Shift-And bit-parallelism.

Fill in the body of `wildcard_search`. Do NOT use `re` or `fnmatch`; implement the
Shift-And automaton with a wildcard mask yourself.
"""

from typing import List


def wildcard_search(text: str, pattern: str) -> List[int]:
    """Return all start indices where `pattern` (with '?' wildcards) matches `text`.

    '?' matches any single character. Non-'?' characters must match exactly. The
    pattern matches a contiguous window of length len(pattern); overlaps allowed.

    Args:
        text: The text to search within (contains no '?').
        pattern: The (non-empty) pattern; '?' matches any single character.

    Returns:
        A sorted list of 0-based start indices of every match. Empty if none.

    Example:
        >>> wildcard_search("abcabd", "a?c")
        [0]
        >>> wildcard_search("mississippi", "is?i")
        [1, 4]

    Approach (Shift-And + wildcard mask):
        - Q = OR of (1 << j) for every position j where pattern[j] == '?'.
        - B[c] = OR of (1 << j) for positions j where pattern[j] == c (c != '?').
        - Scan text; D = ((D << 1) | 1) & (B.get(c, 0) | Q).
        - Whenever bit (m - 1) is set, append (i - m + 1).
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(wildcard_search("abcabd", "a?c"))        # expected: [0]
    print(wildcard_search("mississippi", "is?i"))  # expected: [1, 4]
    print(wildcard_search("xyzxyz", "?y?"))        # expected: [0, 3]
