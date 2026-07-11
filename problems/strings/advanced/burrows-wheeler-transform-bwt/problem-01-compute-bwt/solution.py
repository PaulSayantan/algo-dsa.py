"""Compute the Burrows-Wheeler Transform of a string.

Fill in `bwt` so it returns the last column of the sorted Burrows-Wheeler Matrix.
"""

from typing import List


def bwt(text: str) -> str:
    """Return the Burrows-Wheeler Transform (last column) of ``text``.

    Args:
        text: The input string, terminated by a unique sentinel ``$`` that is
            lexicographically smaller than every other character.

    Returns:
        A string of length ``len(text)`` -- the last column of the matrix formed
        by sorting all cyclic rotations of ``text``.

    Example:
        >>> bwt("banana$")
        'annb$aa'
    """
    # TODO: implement
    pass


def suffix_array(text: str) -> List[int]:
    """(Optional helper) Return the suffix array of ``text``.

    The suffix array is the list of starting indices of ``text`` ordered by the
    lexicographic order of the suffixes they begin. Building the BWT from the
    suffix array via ``L[i] = text[SA[i] - 1]`` avoids materializing rotations.

    Args:
        text: The input string (sentinel-terminated).

    Returns:
        A permutation of ``range(len(text))`` sorted by suffix.
    """
    # TODO: implement (optional; only needed for the efficient approach)
    pass


if __name__ == "__main__":
    # Expected: "annb$aa"
    print(bwt("banana$"))
    # Expected: "ard$rcaaaabb"
    print(bwt("abracadabra$"))
    # Expected: "AA$"
    print(bwt("AA$"))
