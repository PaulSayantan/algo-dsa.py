"""Invert the Burrows-Wheeler Transform.

Fill in `inverse_bwt` so it reconstructs the original string from its BWT.
"""


def inverse_bwt(bwt: str) -> str:
    """Reconstruct the original string from its Burrows-Wheeler Transform.

    Args:
        bwt: The last column ``L`` of the Burrows-Wheeler Matrix of some
            sentinel-terminated string. Contains exactly one ``$`` which is the
            lexicographically smallest character.

    Returns:
        The unique original string ``text`` (ending in ``$``) whose BWT is ``bwt``.

    Example:
        >>> inverse_bwt("annb$aa")
        'banana$'
    """
    # TODO: implement
    # Hint: build the first column F = sorted(bwt); compute the LF-mapping using
    # the fact that the k-th occurrence of a character in L maps to the k-th
    # occurrence of that character in F; then walk the mapping from the '$' row.
    pass


if __name__ == "__main__":
    # Expected: "banana$"
    print(inverse_bwt("annb$aa"))
    # Expected: "abracadabra$"
    print(inverse_bwt("ard$rcaaaabb"))
    # Expected: "AA$"
    print(inverse_bwt("AA$"))
