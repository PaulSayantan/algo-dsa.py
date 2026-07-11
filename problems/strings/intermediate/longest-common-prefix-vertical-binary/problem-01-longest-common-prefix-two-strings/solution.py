"""Longest Common Prefix of Two Strings.

Fill in `longest_common_prefix_pair` so that it returns the longest string that is a
prefix of both `a` and `b`.
"""
from __future__ import annotations


def longest_common_prefix_pair(a: str, b: str) -> str:
    """Return the longest common prefix of two strings.

    Args:
        a: The first string.
        b: The second string.

    Returns:
        The longest string that is a prefix of both `a` and `b`. Returns "" when the
        first characters differ or when either input is empty.

    Example:
        >>> longest_common_prefix_pair("flower", "flight")
        'fl'
        >>> longest_common_prefix_pair("dog", "cat")
        ''
    """
    # TODO: implement (vertical scan up to min length, or binary search on prefix length)
    pass


if __name__ == "__main__":
    print(longest_common_prefix_pair("flower", "flight"))        # expected: "fl"
    print(longest_common_prefix_pair("dog", "cat"))              # expected: ""
    print(longest_common_prefix_pair("interspecies", "interstellar"))  # expected: "inters"
    print(longest_common_prefix_pair("abc", "abcde"))            # expected: "abc"
