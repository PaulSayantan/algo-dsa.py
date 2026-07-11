"""Count Pattern Occurrences.

Preprocess a fixed text S with a suffix array, then answer, for each query
pattern P, how many times P occurs (overlaps counted) in S using binary search
over the sorted suffixes.
"""
from typing import List


def count_occurrences(s: str, queries: List[str]) -> List[int]:
    """For each pattern in ``queries``, count its occurrences in ``s``.

    Args:
        s: The fixed text to search within.
        queries: A list of pattern strings to count.

    Returns:
        A list of integers; the i-th value is the number of (possibly
        overlapping) occurrences of ``queries[i]`` in ``s``.

    Example:
        >>> count_occurrences("banana", ["ana", "na", "x"])
        [2, 2, 0]
    """
    # TODO: build the suffix array of s, then for each pattern do two binary
    # searches (lower/upper bound) to find the contiguous block of suffixes
    # that start with the pattern; the count is the block width.
    pass


if __name__ == "__main__":
    print(count_occurrences("banana", ["ana", "na", "x"]))          # expected: [2, 2, 0]
    print(count_occurrences("mississippi", ["issi", "ss", "i"]))     # expected: [2, 2, 4]
    print(count_occurrences("aaaa", ["aa", "aaaa", "aaaaa"]))        # expected: [3, 1, 0]
