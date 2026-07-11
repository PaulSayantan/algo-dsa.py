"""Locate every start position of a pattern using an FM-index + suffix array.

Fill in `locate` so it returns the sorted list of 0-based start indices where
`pattern` occurs in `text`.
"""

from typing import List


def locate(text: str, pattern: str) -> List[int]:
    """Return all sorted 0-based start indices of ``pattern`` in ``text``.

    Args:
        text: The text to search, terminated by a unique smallest sentinel ``$``.
        pattern: The query string (does not contain ``$``).

    Returns:
        A sorted list of 0-based start positions of ``pattern`` in ``text``;
        an empty list if the pattern does not occur.

    Example:
        >>> locate("banana$", "ana")
        [1, 3]
    """
    # TODO: implement
    # Suggested plan:
    #   1. Build the suffix array SA of text.
    #   2. Build the BWT L where L[i] = text[SA[i] - 1].
    #   3. Build the FM-index (C[] and rank Occ) over L.
    #   4. Backward-search the pattern to get the row range [top, bottom].
    #   5. Return sorted(SA[top .. bottom]); [] if the range is empty.
    pass


if __name__ == "__main__":
    # Expected: [1, 3]
    print(locate("banana$", "ana"))
    # Expected: [1, 4]
    print(locate("mississippi$", "issi"))
    # Expected: []
    print(locate("banana$", "z"))
