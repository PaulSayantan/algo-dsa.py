"""Longest Matchable Suffix with an FM-Index.

For a pattern P, find the length of the longest suffix of P that occurs as a
substring of the indexed text T, using a single partial backward search.
"""
from typing import Dict, List


class FMIndex:
    """FM-Index exposing a partial backward search over the BWT."""

    def __init__(self, text: str, sentinel: str = "$") -> None:
        """Build the FM-Index for `text`.

        Args:
            text: The text to index (must not contain the sentinel character).
            sentinel: A character smaller than every character of `text`.
        """
        # TODO: implement
        #   Build S = text + sentinel, its suffix array, the BWT,
        #   the C[] table, and the prefix-rank table occ[][].
        pass

    def _rank(self, c: str, i: int) -> int:
        """Return occurrences of `c` in BWT[0:i] (0 if `c` is not in the text)."""
        # TODO: implement
        pass

    def longest_matchable_suffix(self, pattern: str) -> int:
        """Return the length of the longest suffix of `pattern` that occurs in T.

        Args:
            pattern: The query pattern.

        Returns:
            The largest L such that pattern[len(pattern)-L:] is a substring of T;
            0 if even the last character of `pattern` is absent from T.

        Example:
            >>> FMIndex("mississippi").longest_matchable_suffix("xsip")
            3
        """
        # TODO: implement partial backward search
        #   sp, ep = 0, n; matched = 0
        #   for c in reversed(pattern):
        #       nsp = C[c] + rank(c, sp); nep = C[c] + rank(c, ep)
        #       if c not in C or nsp >= nep: break
        #       sp, ep = nsp, nep; matched += 1
        #   return matched
        pass


if __name__ == "__main__":
    fm = FMIndex("mississippi")
    print(fm.longest_matchable_suffix("xsip"))  # expected: 3
    print(fm.longest_matchable_suffix("ssis"))  # expected: 4
    print(fm.longest_matchable_suffix("xyz"))   # expected: 0
