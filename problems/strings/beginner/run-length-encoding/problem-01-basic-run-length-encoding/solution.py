"""Basic Run-Length Encoding.

Compress a string by replacing each maximal run of identical characters with
that character followed by the run length in decimal.
"""


def run_length_encode(s: str) -> str:
    """Encode ``s`` using Run-Length Encoding.

    Args:
        s: The input string. Contains only letters (no digits), so counts in
            the output are unambiguous. May be empty.

    Returns:
        The RLE-compressed string where each run "cccc" becomes "c" + str(len).
        For example "aaabbc" -> "a3b2c1".

    Example:
        >>> run_length_encode("aaabbc")
        'a3b2c1'
        >>> run_length_encode("")
        ''
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(run_length_encode("aaabbc"))       # expected: "a3b2c1"
    print(run_length_encode("abc"))          # expected: "a1b1c1"
    print(run_length_encode("wwwwwwwwwwww"))  # expected: "w12"
    print(run_length_encode(""))             # expected: ""
