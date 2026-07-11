"""Wildcard single-character (`?`) matching with Bitap.

Fill in `wildcard_search` yourself. This file is an empty template on purpose.
"""

from __future__ import annotations

from typing import List


def wildcard_search(text: str, pattern: str) -> List[int]:
    """Return all start indices where `pattern` matches, treating '?' as any char.

    Solve this with the Bitap shift-and register plus a wildcard mask:
      1. Build `peq[c]`: bit j set iff pattern[j] == c (literal characters only).
      2. Build `wildcard`: bit j set iff pattern[j] == '?'.
      3. Sweep R over the text with
             R = ((R << 1) | 1) & (peq[c] | wildcard)
         so '?' positions are never cleared.
      4. Whenever bit `1 << (len(pattern) - 1)` is set in R, a match ends at the
         current index i; record start index `i - len(pattern) + 1`.

    Args:
        text:    The text to search (lowercase English letters).
        pattern: The pattern of lowercase letters and '?' wildcards.

    Returns:
        A list of 0-based start indices in ascending order (empty if no match).

    Example:
        >>> wildcard_search("abcabcabc", "a?c")
        [0, 3, 6]
    """
    # TODO: implement using the Bitap shift-and register with a wildcard mask.
    pass


if __name__ == "__main__":
    print(wildcard_search("abcabcabc", "a?c"))   # expected: [0, 3, 6]
    print(wildcard_search("mississippi", "?ss")) # expected: [1, 4]
    print(wildcard_search("hello", "h?llo"))     # expected: [0]
    print(wildcard_search("abcde", "x?z"))       # expected: []
