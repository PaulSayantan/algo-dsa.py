"""Longest Common Substring of Two Strings.

Find the longest contiguous substring present in both A and B. Concatenate
T = A + '#' + B, build its suffix array and LCP array, and take the max LCP over
adjacent suffix pairs that originate from different source strings.
"""


def longest_common_substring(a: str, b: str) -> str:
    """Return a longest substring occurring in both ``a`` and ``b``.

    Args:
        a: First string.
        b: Second string.

    Returns:
        A longest common contiguous substring of ``a`` and ``b``. Returns "" if
        they share no substring. If several are tied, any one is acceptable.

    Example:
        >>> longest_common_substring("banana", "ananas")
        'anana'
    """
    # TODO:
    #   1. Build t = a + sep + b with a separator not in a or b.
    #   2. Build the suffix array and LCP array of t.
    #   3. For each adjacent sorted pair, if one suffix starts in a and the other
    #      in b, consider its LCP; track the maximum and its start index.
    #   4. Return the substring of that maximum length.
    pass


if __name__ == "__main__":
    print(longest_common_substring("banana", "ananas"))   # expected: "anana"
    print(longest_common_substring("abcde", "cdefg"))       # expected: "cde"
    print(longest_common_substring("abc", "xyz"))           # expected: ""
