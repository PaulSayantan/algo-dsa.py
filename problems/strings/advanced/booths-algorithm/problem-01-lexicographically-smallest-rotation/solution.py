"""Lexicographically Smallest Rotation.

Return the lexicographically smallest rotation of the input string in O(n) time
using Booth's Algorithm.
"""


def smallest_rotation(s: str) -> str:
    """Return the lexicographically smallest rotation of ``s``.

    A rotation ``i`` of ``s`` is ``s[i:] + s[:i]``. Among all ``len(s)``
    rotations, return the one that is smallest in dictionary order.

    Args:
        s: The input string (fixed, totally ordered alphabet).

    Returns:
        The lexicographically smallest rotation of ``s`` as a string. For the
        empty string, return the empty string.

    Example:
        >>> smallest_rotation("cba")
        'acb'
        >>> smallest_rotation("abab")
        'abab'
    """
    # TODO: implement (hint: Booth's Algorithm — run a modified KMP failure
    # function over s + s to find the start index of the least rotation, then
    # return s[k:] + s[:k]).
    pass


if __name__ == "__main__":
    print(smallest_rotation("cba"))          # expected: "acb"
    print(smallest_rotation("bbaaccaadd"))   # expected: "aaccaaddbb"
    print(smallest_rotation("abab"))         # expected: "abab"
    print(smallest_rotation("baaca"))        # expected: "aacab"
