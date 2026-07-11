"""Check if a String is a Lyndon Word.

Fill in `is_lyndon` using Lyndon Factorization (Duval's algorithm): a string is a
Lyndon word iff its factorization is a single factor equal to the whole string.
"""
from __future__ import annotations


def is_lyndon(s: str) -> bool:
    """Return whether `s` is a Lyndon word.

    A Lyndon word is strictly smaller than all of its proper suffixes
    (equivalently, strictly smaller than all of its non-trivial rotations).

    Args:
        s: A non-empty string of lowercase English letters.

    Returns:
        True if `s` is a Lyndon word, False otherwise.

    Example:
        >>> is_lyndon("aab")
        True
        >>> is_lyndon("abab")
        False
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(is_lyndon("aab"))   # expected: True
    print(is_lyndon("abab"))  # expected: False
    print(is_lyndon("b"))     # expected: True
