"""Substring Equality Queries.

Answer many "are these two equal-length substrings identical?" queries in O(1)
each, using polynomial PREFIX hashing built in O(n).
"""

from typing import List, Tuple


def substring_equality_queries(
    s: str, queries: List[Tuple[int, int, int]]
) -> List[bool]:
    """Answer substring-equality queries with prefix polynomial hashing.

    Args:
        s: The source string (lowercase English letters).
        queries: A list of ``(a, b, length)`` tuples. Each asks whether
            ``s[a : a + length]`` equals ``s[b : b + length]``. Every query is
            guaranteed to stay within bounds.

    Returns:
        A list of booleans, one per query, where entry ``i`` is ``True`` iff the
        two substrings referenced by ``queries[i]`` are equal.

    Example:
        >>> substring_equality_queries("ababab", [(0, 2, 2), (0, 1, 2)])
        [True, False]
    """
    # TODO: implement using polynomial prefix hashing.
    #   1. Build prefix hashes H[0..n] and powers of the base modulo a prime.
    #   2. For a query (a, b, length), compare hash(s[a:a+length]) with
    #      hash(s[b:b+length]) in O(1). (Optionally verify on a hash hit, or use
    #      double hashing to make collisions negligible.)
    pass


if __name__ == "__main__":
    print(substring_equality_queries("ababab", [(0, 2, 2), (0, 1, 2), (0, 2, 4)]))
    # expected: [True, False, True]
    print(substring_equality_queries("aaaaa", [(0, 1, 3), (2, 2, 2), (0, 3, 2)]))
    # expected: [True, True, True]
