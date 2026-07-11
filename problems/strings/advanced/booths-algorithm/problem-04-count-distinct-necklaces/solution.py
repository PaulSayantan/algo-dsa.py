"""Count Distinct Necklaces.

Two strings are the same necklace iff one is a rotation of the other. Count the
number of distinct necklaces by canonicalizing each string to its smallest
rotation (Booth's Algorithm) and deduplicating.
"""

from typing import List


def count_distinct_necklaces(words: List[str]) -> int:
    """Return the number of distinct necklaces (strings up to rotation).

    Args:
        words: A list of strings. Strings of different lengths are always
            distinct necklaces; strings that are rotations of one another count
            as a single necklace.

    Returns:
        The count of distinct necklaces.

    Example:
        >>> count_distinct_necklaces(["abc", "bca", "cab", "xyz"])
        2
        >>> count_distinct_necklaces(["aa", "aaa", "aaaa"])
        3
    """
    # TODO: implement
    #   For each word, compute its canonical form = lexicographically smallest
    #   rotation (Booth's Algorithm), then count distinct canonical forms.
    pass


if __name__ == "__main__":
    print(count_distinct_necklaces(["abc", "bca", "cab", "xyz"]))          # expected: 2
    print(count_distinct_necklaces(["abab", "baba", "ab", "ba", "abc"]))   # expected: 3
    print(count_distinct_necklaces(["aa", "aaa", "aaaa"]))                 # expected: 3
