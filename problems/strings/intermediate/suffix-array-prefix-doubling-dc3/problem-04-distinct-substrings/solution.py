"""Number of Distinct Substrings.

Count distinct non-empty substrings of S. Build the suffix array and LCP array;
the answer is n*(n+1)//2 - sum(LCP).
"""


def count_distinct_substrings(s: str) -> int:
    """Count the number of distinct non-empty substrings of ``s``.

    Args:
        s: The input string.

    Returns:
        The number of distinct non-empty substrings of ``s`` as an integer.

    Example:
        >>> count_distinct_substrings("banana")
        15
    """
    # TODO: build the suffix array and LCP array, then return
    #   n * (n + 1) // 2 - sum(lcp)
    pass


if __name__ == "__main__":
    print(count_distinct_substrings("banana"))   # expected: 15
    print(count_distinct_substrings("aaa"))       # expected: 3
    print(count_distinct_substrings("abc"))       # expected: 6
