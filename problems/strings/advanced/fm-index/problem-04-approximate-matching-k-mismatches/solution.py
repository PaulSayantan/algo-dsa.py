"""Approximate Matching with k Mismatches using an FM-Index.

Count alignment start positions where a pattern matches the text within Hamming
distance k, using a branching backward search over the BWT.
"""
from typing import Dict, List


class FMIndex:
    """FM-Index supporting exact and approximate (k-mismatch) matching."""

    def __init__(self, text: str, sentinel: str = "$") -> None:
        """Build the FM-Index for `text`.

        Args:
            text: The text to index (must not contain the sentinel character).
            sentinel: A character smaller than every character of `text`.
        """
        # TODO: implement
        #   Build S = text + sentinel, its suffix array, the BWT, the C[] table,
        #   the prefix-rank table occ[][], and store the alphabet (excluding '$').
        pass

    def _rank(self, c: str, i: int) -> int:
        """Return occurrences of `c` in BWT[0:i] (0 if `c` is not in the text)."""
        # TODO: implement
        pass

    def count_k_mismatches(self, pattern: str, k: int) -> int:
        """Count alignments of `pattern` in T with at most `k` Hamming mismatches.

        Args:
            pattern: The pattern to align (fixed length m).
            k: Maximum number of allowed mismatches.

        Returns:
            The number of start positions i in [0, n-m] such that pattern and
            T[i:i+m] differ in at most k positions (overlaps counted separately).

        Example:
            >>> FMIndex("acgtacgt").count_k_mismatches("aca", 1)
            2
        """
        # TODO: implement branching backward search
        #   Recurse over positions m-1 .. 0 carrying (sp, ep, budget).
        #   At each position try every alphabet character c:
        #       nsp = C[c] + rank(c, sp); nep = C[c] + rank(c, ep)
        #       if nsp >= nep: prune
        #       nb = budget - (0 if c == pattern[pos] else 1)
        #       if nb < 0: prune
        #       recurse(pos-1, nsp, nep, nb)
        #   When pos < 0, add (ep - sp) to the running total.
        pass


if __name__ == "__main__":
    fm = FMIndex("acgtacgt")
    print(fm.count_k_mismatches("acg", 0))  # expected: 2
    print(fm.count_k_mismatches("aca", 1))  # expected: 2
    fm2 = FMIndex("mississippi")
    print(fm2.count_k_mismatches("issa", 1))  # expected: 2
