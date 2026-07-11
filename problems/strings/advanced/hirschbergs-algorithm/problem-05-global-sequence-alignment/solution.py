"""Global (Needleman-Wunsch) sequence alignment in O(min(n, m)) space.

Fill in `align`. Return the two aligned strings (with '-' gap characters) whose
column score is maximal under (match, mismatch, gap). Use Hirschberg's
divide-and-conquer so you never store the full (n+1)*(m+1) DP table.

Scoring per column:
    match     if the two characters are equal
    mismatch  if they differ
    gap       if either side is '-'
"""

from typing import List, Tuple


def nw_score_row(a: str, b: str, match: int, mismatch: int, gap: int) -> List[int]:
    """Return the last row of the Needleman-Wunsch score DP for `a` vs `b`.

    result[j] = best alignment score of `a` against `b[:j]`.

    Args:
        a: String indexing DP rows.
        b: String indexing DP columns.
        match: Score for aligning two equal characters.
        mismatch: Score for aligning two differing characters.
        gap: Score for aligning a character against a gap.

    Returns:
        A list of length len(b) + 1, one rolling row of best scores.
    """
    # TODO: implement the single-rolling-row NW score pass (with gap-initialized borders)
    pass


def align(a: str, b: str, match: int = 1, mismatch: int = -1,
          gap: int = -2) -> Tuple[str, str]:
    """Return an optimal global alignment (aligned_a, aligned_b) of `a` and `b`.

    Args:
        a: First string.
        b: Second string.
        match: Score for a matching column.
        mismatch: Score for a mismatching column.
        gap: Penalty (negative) for a gap column.

    Returns:
        A pair of equal-length strings over the alphabet plus '-'; removing '-'
        from the first yields `a`, and from the second yields `b`. The column
        score is maximal. Any optimal alignment is acceptable.

    Example:
        >>> align("TACG", "TCG", 1, -1, -2)
        ('TACG', 'T-CG')
    """
    # TODO: implement Hirschberg's divide-and-conquer alignment traceback
    pass


if __name__ == "__main__":
    a1, b1 = align("TACG", "TCG", 1, -1, -2)
    print(a1)  # expected e.g. "TACG"
    print(b1)  # expected e.g. "T-CG"  (optimal score 1)
    a2, b2 = align("AGTA", "ATA", 1, -1, -2)
    print(a2)  # expected e.g. "AGTA"
    print(b2)  # expected e.g. "A-TA"  (optimal score 1)
