"""Edit distance with recovered operations, in O(min(n, m)) space.

Fill in `edit_script`. Return the minimum cost and an ordered edit script that
transforms word1 into word2. Use Hirschberg's divide-and-conquer so you never
materialise the full traceback table.

Operation encoding (suggested):
    ("match",   c)         keep character c (cost 0)
    ("replace", c1, c2)    change c1 into c2 (cost 1)
    ("delete",  c1)        remove c1 from word1 (cost 1)
    ("insert",  c2)        add c2 from word2 (cost 1)
"""

from typing import List, Tuple

Op = Tuple  # e.g. ("match", "a") or ("replace", "a", "b")


def edit_cost_row(a: str, b: str) -> List[int]:
    """Return the last row of the Levenshtein DP for transforming `a` into `b`.

    result[j] = edit distance between `a` and `b[:j]`.

    Args:
        a: Source string (indexes DP rows).
        b: Target string (indexes DP columns).

    Returns:
        A list of length len(b) + 1, one rolling row of edit distances.

    Example:
        >>> edit_cost_row("ab", "abc")
        [2, 1, 0, 1]
    """
    # TODO: implement the single-rolling-row Levenshtein cost pass
    pass


def edit_script(word1: str, word2: str) -> Tuple[int, List[Op]]:
    """Return (minimum edit cost, ordered edit script) turning word1 into word2.

    Args:
        word1: Source string.
        word2: Target string.

    Returns:
        A tuple (cost, ops) where cost is the Levenshtein distance and ops is a
        left-to-right list of operations. Any optimal script is acceptable.

    Example:
        >>> cost, ops = edit_script("horse", "ros")
        >>> cost
        3
    """
    # TODO: implement Hirschberg's divide-and-conquer traceback for edit distance
    pass


if __name__ == "__main__":
    c1, ops1 = edit_script("horse", "ros")
    print(c1)  # expected: 3
    c2, ops2 = edit_script("intention", "execution")
    print(c2)  # expected: 5
    c3, ops3 = edit_script("", "abc")
    print(c3)  # expected: 3
