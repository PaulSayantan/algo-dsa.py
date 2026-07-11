"""Locate Substring Occurrences with an FM-Index.

Build an index over a fixed text `T` once, then report every start index of a
pattern via backward search plus a suffix-array lookup.
"""
from typing import Dict, List, Tuple


class FMIndex:
    """FM-Index supporting locate queries (all start positions of a pattern)."""

    def __init__(self, text: str, sentinel: str = "$") -> None:
        """Build the FM-Index for `text`.

        Args:
            text: The text to index (must not contain the sentinel character).
            sentinel: A character smaller than every character of `text`.
        """
        # TODO: implement
        #   Build S = text + sentinel, its suffix array, the BWT,
        #   the C[] table, and the prefix-rank table occ[][].
        #   Keep the suffix array around so locate() can map rows -> positions.
        pass

    def _rank(self, c: str, i: int) -> int:
        """Return occurrences of `c` in BWT[0:i] (0 if `c` is not in the text)."""
        # TODO: implement
        pass

    def _bw_range(self, pattern: str) -> Tuple[int, int]:
        """Return the half-open suffix-array interval [sp, ep) matching `pattern`.

        Args:
            pattern: The pattern to search for.

        Returns:
            A tuple (sp, ep). The pattern is absent iff sp >= ep.
        """
        # TODO: implement backward search
        pass

    def locate(self, pattern: str) -> List[int]:
        """Return every start index of `pattern` in the text, ascending.

        Args:
            pattern: The pattern to locate.

        Returns:
            Sorted list of 0-based start indices; empty if `pattern` is absent.

        Example:
            >>> FMIndex("mississippi").locate("issi")
            [1, 4]
        """
        # TODO: implement
        #   sp, ep = self._bw_range(pattern)
        #   return sorted(self.sa[i] for i in range(sp, ep))
        pass


def locate_all(text: str, queries: List[str]) -> List[List[int]]:
    """Answer a batch of locate queries against `text`.

    Args:
        text: The fixed text to index.
        queries: Patterns to locate.

    Returns:
        A list of sorted position lists, one per query.
    """
    # TODO: build one FMIndex(text) and map locate() over queries
    pass


if __name__ == "__main__":
    print(locate_all("mississippi", ["issi", "ss", "i", "ppi"]))
    # expected: [[1, 4], [2, 5], [1, 4, 7, 10], [8]]
    print(locate_all("aaaa", ["aa", "aaa", "b"]))
    # expected: [[0, 1, 2], [0, 1], []]
