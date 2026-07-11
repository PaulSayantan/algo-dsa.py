"""Lyndon Factorization of a String.

Implement `lyndon_factorization` with Duval's algorithm so that it returns the unique
non-increasing sequence of Lyndon factors whose concatenation is `s`.
"""
from __future__ import annotations

from typing import List


def lyndon_factorization(s: str) -> List[str]:
    """Return the Chen-Fox-Lyndon factorization of `s`.

    The result is a list of Lyndon words w1, w2, ..., wk such that
    w1 >= w2 >= ... >= wk lexicographically and their concatenation equals `s`.

    Args:
        s: A non-empty string of lowercase English letters.

    Returns:
        The list of Lyndon factors in non-increasing order.

    Example:
        >>> lyndon_factorization("banana")
        ['b', 'an', 'an', 'a']
        >>> lyndon_factorization("abacaba")
        ['abac', 'ab', 'a']
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(lyndon_factorization("banana"))   # expected: ['b', 'an', 'an', 'a']
    print(lyndon_factorization("abacaba"))  # expected: ['abac', 'ab', 'a']
    print(lyndon_factorization("aaa"))      # expected: ['a', 'a', 'a']
