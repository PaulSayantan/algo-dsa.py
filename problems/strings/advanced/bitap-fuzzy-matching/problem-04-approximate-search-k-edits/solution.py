"""Approximate search within k edits (Levenshtein) using the Wu-Manber Bitap.

Fill in `approx_search` yourself. This file is an empty template on purpose.
"""

from __future__ import annotations

from typing import List


def approx_search(text: str, pattern: str, k: int) -> List[int]:
    """Return end positions where `pattern` occurs within `k` edits.

    Edits are insertions, deletions, and substitutions (Levenshtein distance).
    Report every index e such that SOME substring of `text` ending at e
    (inclusive) is within edit distance k of `pattern`.

    Solve this with the Wu-Manber Bitap recurrence:
      1. Build `peq[c]`: bit j set iff pattern[j] == c.
      2. Initialize k+1 registers with R[d] = (1 << d) - 1 (low d bits set),
         which allows deleting the first d pattern characters for free.
      3. For each text char c, updating from d = 0 upward and keeping `oldR[d-1]`
         (the value R[d-1] had before this char):
             R[0] = ((oldR[0] << 1) | 1) & peq[c]
             R[d] = (((oldR[d] << 1) | 1) & peq[c])   # match / substitution base
                    | ((oldR[d-1] | R[d-1]) << 1)     # substitution + insertion
                    | oldR[d-1]                        # deletion
                    | 1
      4. When bit `1 << (len(pattern) - 1)` of R[k] is set, a match ends at
         index i; record i.

    Args:
        text:    The text to search.
        pattern: The pattern to match (length <= 64).
        k:       Maximum allowed edit distance (0 <= k <= len(pattern)).

    Returns:
        Sorted list of 0-based inclusive end positions (empty if none).

    Example:
        >>> approx_search("hello", "help", 1)
        [2, 3]
    """
    # TODO: implement using k+1 Bitap registers with the Wu-Manber recurrence.
    pass


if __name__ == "__main__":
    print(approx_search("approximatly", "approximately", 1))  # expected: [11]
    print(approx_search("banana", "anna", 1))                 # expected: [3, 5]
    print(approx_search("hello", "help", 1))                  # expected: [2, 3]
