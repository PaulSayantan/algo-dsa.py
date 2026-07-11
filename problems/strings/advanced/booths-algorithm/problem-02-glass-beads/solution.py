"""Glass Beads (UVa 719 / POJ 1509).

Given a cyclic string, return the 1-based starting position of the
lexicographically smallest rotation, using Booth's Algorithm in O(n).
"""


def cut_position(s: str) -> int:
    """Return the 1-based index where the smallest rotation of ``s`` begins.

    Among all len(s) rotations, find the lexicographically smallest one. Return
    the 1-based starting position in ``s`` where it begins. If several positions
    tie (periodic ``s``), return the smallest such position.

    Args:
        s: The necklace as a string of lowercase letters ('a' is smallest).

    Returns:
        A 1-based index in [1, len(s)].

    Example:
        >>> cut_position("helloworld")
        10
        >>> cut_position("abab")
        1
    """
    # TODO: implement (hint: Booth's Algorithm gives the 0-based least-rotation
    # start index; return that index + 1).
    pass


if __name__ == "__main__":
    print(cut_position("helloworld"))     # expected: 10
    print(cut_position("abab"))           # expected: 1
    print(cut_position("dontcallmebfu"))  # expected: 6
    print(cut_position("aaabaaa"))        # expected: 5
