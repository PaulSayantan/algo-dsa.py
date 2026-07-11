"""Count Substring Occurrences with an FM-Index.

Build an index over a fixed text `T` once, then answer many `count(P)` queries,
each in O(|P|) time using backward search over the Burrows-Wheeler Transform.
"""
from typing import Dict, List


class FMIndex:
    """FM-Index over a text, supporting occurrence counting via backward search.

    The index appends a unique sentinel '$' (lexicographically smallest) to the
    text, builds the BWT, and precomputes:
      - C[c]:   number of characters in the text strictly less than c
      - occ[c]: prefix-rank table, occ[c][i] = count of c in BWT[0:i]
    """

    def __init__(self, text: str, sentinel: str = "$") -> None:
        """Build the FM-Index for `text`.

        Args:
            text: The text to index (must not contain the sentinel character).
            sentinel: A character smaller than every character of `text`.
        """
        # TODO: implement
        #   1. self.s = text + sentinel
        #   2. build the suffix array of self.s
        #   3. BWT[i] = self.s[(sa[i] - 1) % n]
        #   4. build C[] and the prefix-rank table occ[][]
        pass

    def _rank(self, c: str, i: int) -> int:
        """Return the number of occurrences of `c` in BWT[0:i] (0 if c unseen).

        Args:
            c: A single character.
            i: A prefix length into the BWT (0 <= i <= n).

        Returns:
            Count of `c` among the first `i` BWT characters.
        """
        # TODO: implement
        pass

    def count(self, pattern: str) -> int:
        """Return the number of occurrences of `pattern` in the indexed text.

        Args:
            pattern: The pattern to search for (overlaps counted).

        Returns:
            The occurrence count; 0 if `pattern` does not occur.

        Example:
            >>> FMIndex("mississippi").count("issi")
            2
        """
        # TODO: implement backward search
        #   sp, ep = 0, n
        #   for c in reversed(pattern):
        #       sp = C[c] + rank(c, sp)
        #       ep = C[c] + rank(c, ep)
        #       if sp >= ep: return 0
        #   return ep - sp
        pass


def count_occurrences(text: str, queries: List[str]) -> List[int]:
    """Answer a batch of occurrence-count queries against `text`.

    Args:
        text: The fixed text to index.
        queries: Patterns to count.

    Returns:
        A list whose i-th entry is the occurrence count of queries[i].
    """
    # TODO: build one FMIndex(text) and map count() over queries
    pass


if __name__ == "__main__":
    print(count_occurrences("mississippi", ["issi", "ss", "i", "ppi", "ab"]))
    # expected: [2, 2, 4, 1, 0]
    print(count_occurrences("banana", ["ana", "na", "a", "x"]))
    # expected: [2, 2, 3, 0]
