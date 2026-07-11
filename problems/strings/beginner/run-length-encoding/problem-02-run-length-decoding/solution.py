"""Run-Length Decoding.

Expand an RLE string of the form "<char><count><char><count>..." back into the
original string. Counts may have multiple digits.
"""


def run_length_decode(encoded: str) -> str:
    """Decode a Run-Length Encoded string.

    Args:
        encoded: A valid RLE string. Each block is one non-digit character
            followed by one or more decimal digits (an integer >= 1). May be
            empty.

    Returns:
        The decompressed original string. For example "a3b2c1" -> "aaabbc".

    Example:
        >>> run_length_decode("a3b2c1")
        'aaabbc'
        >>> run_length_decode("w12")
        'wwwwwwwwwwww'
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(run_length_decode("a3b2c1"))  # expected: "aaabbc"
    print(run_length_decode("w12"))     # expected: "wwwwwwwwwwww"
    print(run_length_decode("x1y1z1"))  # expected: "xyz"
    print(run_length_decode(""))        # expected: ""
