"""Lexicographically Smallest Rotation.

Implement `least_rotation` using Duval's algorithm on the doubled string s + s.
Return the smallest cyclic rotation itself.
"""
from __future__ import annotations


def least_rotation(s: str) -> str:
    """Return the lexicographically smallest rotation of `s`.

    A rotation by d is s[d:] + s[:d]; there are len(s) of them.

    Args:
        s: A non-empty string of lowercase English letters.

    Returns:
        The lexicographically smallest rotation of `s`.

    Example:
        >>> least_rotation("bca")
        'abc'
        >>> least_rotation("baabaa")
        'aabaab'
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(least_rotation("bca"))     # expected: 'abc'
    print(least_rotation("baabaa"))  # expected: 'aabaab'
    print(least_rotation("dcba"))    # expected: 'adcb'
