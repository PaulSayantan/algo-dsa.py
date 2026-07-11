"""Fuzzy substring search allowing k edits (Wu-Manber bit-parallel algorithm).

Fill in the body of `fuzzy_search_ends`. Implement the Wu-Manber recurrence with
k+1 state words; do not fall back to an O(n*m*k) dynamic-programming table.
"""

from typing import List


def fuzzy_search_ends(text: str, pattern: str, k: int) -> List[int]:
    """Return all end positions where `pattern` matches within edit distance k.

    An end position `pos` qualifies if some substring of `text` ending at index
    `pos` is within Levenshtein distance `k` of `pattern` (insertions, deletions,
    and substitutions all allowed).

    Args:
        text: The text to search within.
        pattern: The (non-empty) pattern.
        k: Maximum number of allowed edits (k >= 0). k == 0 means exact matching.

    Returns:
        A sorted list of 0-based end indices `pos` in `text` such that a substring
        ending at `pos` is within edit distance k of `pattern`.

    Example:
        >>> fuzzy_search_ends("survey", "surgery", 2)
        [5]
        >>> fuzzy_search_ends("hello", "hallo", 1)
        [4]

    Approach (Wu-Manber):
        - B[c] = OR of (1 << j) for positions j where pattern[j] == c.
        - Initialize R[d] = (1 << d) - 1 for d in 0..k.
        - For each text char c, with old = snapshot of R and new the next values:
              new[0] = ((old[0] << 1) | 1) & B[c]
              new[d] = (((old[d] << 1) | 1) & B[c])   # match / mismatch-advance
                       | old[d - 1]                    # deletion in pattern
                       | ((old[d - 1] << 1) | 1)       # substitution
                       | (new[d - 1] << 1)             # insertion
        - Record `pos` when new[k] has bit (m - 1) set.
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(fuzzy_search_ends("survey", "surgery", 2))  # expected: [5]
    print(fuzzy_search_ends("hello", "hallo", 1))     # expected: [4]
    print(fuzzy_search_ends("hello", "hallo", 0))     # expected: []
    print(fuzzy_search_ends("dog", "cat", 1))         # expected: []
