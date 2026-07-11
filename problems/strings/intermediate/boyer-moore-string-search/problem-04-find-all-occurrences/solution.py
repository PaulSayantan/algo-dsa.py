"""Find All Occurrences of a Pattern.

Return every start index where `pattern` appears in `text`, overlaps included.
Use Boyer–Moore (string search): after a full match, use the good-suffix shift
for a complete match to keep scanning.
"""
from typing import List


def find_all_occurrences(text: str, pattern: str) -> List[int]:
    """Return all 0-based start indices where `pattern` occurs in `text`.

    Overlapping occurrences are all reported, in increasing order.

    Args:
        text: The text to search within.
        pattern: The non-empty pattern to search for.

    Returns:
        A sorted list of every start index of `pattern` in `text`; empty if
        there is no occurrence.

    Example:
        >>> find_all_occurrences("ababab", "ab")
        [0, 2, 4]
        >>> find_all_occurrences("abcxyz", "www")
        []
    """
    # TODO: implement using Boyer–Moore (bad-character + good-suffix rules)
    pass


if __name__ == "__main__":
    print(find_all_occurrences("ababab", "ab"))                  # expected: [0, 2, 4]
    print(find_all_occurrences("aabaacaadaabaaba", "aaba"))      # expected: [0, 9, 12]
    print(find_all_occurrences("abcxyz", "www"))                 # expected: []
