"""Count pattern occurrences using an FM-index built on the BWT.

Fill in `count_occurrences` so it returns, for each query pattern, the number of
times it occurs as a substring of the text whose BWT is given.
"""

from typing import List


def count_occurrences(bwt: str, patterns: List[str]) -> List[int]:
    """Count occurrences of each pattern via FM-index backward search.

    Args:
        bwt: The Burrows-Wheeler Transform of a sentinel-terminated text. Contains
            exactly one ``$`` which is the lexicographically smallest character.
        patterns: Query strings to count. The sentinel never appears inside a
            pattern; a pattern may contain characters absent from the text.

    Returns:
        A list of integers, ``result[k]`` being the number of substring
        occurrences of ``patterns[k]`` in the original text, in input order.

    Example:
        >>> count_occurrences("annb$aa", ["ana", "ban", "na", "x"])
        [2, 1, 2, 0]
    """
    # TODO: implement
    # Suggested plan:
    #   1. Build C[c] = number of characters in bwt strictly smaller than c.
    #   2. Build a rank function Occ(c, i) = number of c in bwt[0..i-1]
    #      (a prefix-count table over the alphabet works well).
    #   3. For each pattern, run backward search maintaining [top, bottom]:
    #         top    = C[c] + Occ(c, top)
    #         bottom = C[c] + Occ(c, bottom + 1) - 1
    #      Stop early (count 0) if top > bottom; else count = bottom - top + 1.
    pass


if __name__ == "__main__":
    # Expected: [2, 1, 2, 0]
    print(count_occurrences("annb$aa", ["ana", "ban", "na", "x"]))
    # Expected: [2, 2, 1, 0]
    print(count_occurrences("ipssm$pissii", ["iss", "ss", "ppi", "z"]))
