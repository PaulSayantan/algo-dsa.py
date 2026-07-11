"""Count Pattern Occurrences (including overlaps).

Fill in the body using Naive Pattern Matching. Count every starting index at
which `pattern` matches, sliding one position at a time so overlaps are
counted. Do not use str.count (it does not count overlapping matches) or
regex.
"""


def count_occurrences(text: str, pattern: str) -> int:
    """Count occurrences of ``pattern`` in ``text``, counting overlaps.

    Args:
        text: The text to search within.
        pattern: The non-empty pattern to search for.

    Returns:
        The number of starting indices ``i`` with
        ``text[i : i + len(pattern)] == pattern``. Overlapping occurrences
        are each counted.

    Example:
        >>> count_occurrences("AABAACAADAABAABA", "AABA")
        3
        >>> count_occurrences("aaaa", "aa")
        3
    """
    # TODO: implement using Naive Pattern Matching
    pass


if __name__ == "__main__":
    print(count_occurrences("AABAACAADAABAABA", "AABA"))  # expected: 3
    print(count_occurrences("aaaa", "aa"))                # expected: 3
    print(count_occurrences("abcabc", "xyz"))             # expected: 0
