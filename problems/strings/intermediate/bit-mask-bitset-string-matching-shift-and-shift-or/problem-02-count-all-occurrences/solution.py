"""Find all (overlapping) occurrences of a pattern using Shift-And bit-parallelism.

Fill in the body of `find_all_occurrences`. Do NOT use `str.find` in a loop or
regex; implement the bitmask automaton so that overlapping matches are reported in
a single left-to-right scan.
"""

from typing import List


def find_all_occurrences(text: str, pattern: str) -> List[int]:
    """Return every start index where `pattern` occurs in `text`, ascending.

    Overlapping occurrences must all be reported.

    Args:
        text: The text to search within.
        pattern: The (non-empty) pattern to search for.

    Returns:
        A sorted list of 0-based start indices of every occurrence of `pattern`
        in `text`. Empty list if there are no occurrences.

    Example:
        >>> find_all_occurrences("abababab", "abab")
        [0, 2, 4]
        >>> find_all_occurrences("aaaaa", "aa")
        [0, 1, 2, 3]

    Approach (Shift-And):
        - B[c] = OR of (1 << j) for positions j where pattern[j] == c.
        - Scan text; D = ((D << 1) | 1) & B.get(c, 0).
        - Whenever bit (m - 1) of D is set, append (i - m + 1) and continue.
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(find_all_occurrences("abababab", "abab"))    # expected: [0, 2, 4]
    print(find_all_occurrences("aaaaa", "aa"))          # expected: [0, 1, 2, 3]
    print(find_all_occurrences("ababcabab", "abab"))    # expected: [0, 5]
