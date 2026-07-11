"""k-mismatch (Hamming distance) substring search with Bitap.

Fill in `k_mismatch_search` yourself. This file is an empty template on purpose.
"""

from __future__ import annotations

from typing import List


def k_mismatch_search(text: str, pattern: str, k: int) -> List[int]:
    """Return start indices where `pattern` matches within `k` substitutions.

    Solve this with the multi-register (Hamming) Bitap:
      1. Build `peq[c]`: bit j set iff pattern[j] == c.
      2. Keep k+1 registers R[0..k], all starting at 0.
      3. For each text char c, update from d = 0 upward. Let `prev` hold the
         value R[d-1] had BEFORE this character (use a saved copy so you do not
         read the already-updated R[d-1]):
             R[0] = ((R[0] << 1) | 1) & peq[c]
             R[d] = (((R[d] << 1) | 1) & peq[c])  # extend a d-mismatch match
                    | (prev << 1)                 # spend one mismatch on this char
                    | 1                           # allow starting fresh here
      4. When bit `1 << (m - 1)` of R[k] is set, a match with <= k mismatches
         ends at index i; its start index is `i - m + 1`.

    Args:
        text:    The text to search.
        pattern: The pattern to match (length <= 64).
        k:       Maximum allowed number of mismatched positions (0 <= k <= m).

    Returns:
        Sorted list of 0-based start indices with Hamming distance <= k
        (empty if none).

    Example:
        >>> k_mismatch_search("aaaaa", "aa", 1)
        [0, 1, 2, 3]
    """
    # TODO: implement using k+1 Bitap registers under Hamming distance.
    pass


if __name__ == "__main__":
    print(k_mismatch_search("GCATCGCAGAGAGTATACAGTACG", "GCAGAGAG", 1))  # expected: [5]
    print(k_mismatch_search("aaaaa", "aa", 1))                          # expected: [0, 1, 2, 3]
    print(k_mismatch_search("abcde", "xbz", 1))                         # expected: []
