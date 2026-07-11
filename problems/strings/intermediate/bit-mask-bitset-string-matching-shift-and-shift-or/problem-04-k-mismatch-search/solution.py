"""k-mismatch (Hamming distance) search using bit-parallel Shift-And.

Fill in the body of `k_mismatch_search`. Implement the (k+1)-word Shift-And ladder;
do not fall back to an O(n*m) per-window character comparison.
"""

from typing import List


def k_mismatch_search(text: str, pattern: str, k: int) -> List[int]:
    """Return all start indices of length-m windows within Hamming distance k.

    A window text[i : i+m] qualifies if it differs from `pattern` in at most `k`
    positions (substitutions only; equal lengths, no insert/delete).

    Args:
        text: The text to search within.
        pattern: The (non-empty) pattern.
        k: Maximum number of allowed mismatches (k >= 0). k == 0 means exact.

    Returns:
        A sorted list of 0-based start indices i such that the Hamming distance
        between text[i : i+len(pattern)] and pattern is <= k.

    Example:
        >>> k_mismatch_search("abcde", "xbcdx", 2)
        [0]
        >>> k_mismatch_search("hello", "jello", 1)
        [0]

    Approach (Shift-And ladder of k+1 words):
        - B[c] = OR of (1 << j) for positions j where pattern[j] == c.
        - Keep R[0..k]. For each text char c (with old = snapshot of R):
              R[0] = ((old[0] << 1) | 1) & B[c]
              R[d] = (((old[d] << 1) | 1) & B[c]) | ((old[d-1] << 1) | 1)   for d>=1
        - A match ends at i when R[k] has bit (m - 1) set; start = i - m + 1.
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(k_mismatch_search("abcde", "xbcdx", 2))  # expected: [0]
    print(k_mismatch_search("abcde", "xbcdx", 1))  # expected: []
    print(k_mismatch_search("hello", "jello", 1))  # expected: [0]
    print(k_mismatch_search("hello", "world", 2))  # expected: []
