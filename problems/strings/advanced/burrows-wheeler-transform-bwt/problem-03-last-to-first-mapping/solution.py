"""Compute the Last-to-First (LF) mapping of a BWT string.

Fill in `lf_mapping` so it returns the LF array described in PROBLEM.md.
"""

from typing import List


def lf_mapping(bwt: str) -> List[int]:
    """Return the Last-to-First mapping array for the BWT string ``bwt``.

    ``LF[i]`` is the row index in the sorted first column that holds the same
    occurrence of ``bwt[i]`` as row ``i`` holds in the last column. Formally,
    ``LF[i] = C[bwt[i]] + (count of bwt[i] in bwt[0..i-1])`` where ``C[c]`` is the
    number of characters in ``bwt`` strictly smaller than ``c``.

    Args:
        bwt: The last column of a Burrows-Wheeler Matrix; contains exactly one
            ``$`` which is the lexicographically smallest character.

    Returns:
        A list of length ``len(bwt)`` and a permutation of ``range(len(bwt))``.

    Example:
        >>> lf_mapping("annb$aa")
        [1, 5, 6, 4, 0, 2, 3]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    # Expected: [1, 5, 6, 4, 0, 2, 3]
    print(lf_mapping("annb$aa"))
    # Expected: [1, 5, 6, 2, 0, 3, 4]
    print(lf_mapping("abba$aa"))
