"""Best fuzzy match (minimum edits) using Bitap as a bounded-edit oracle.

Fill in `min_edits_to_substring` yourself. This file is an empty template.
"""

from __future__ import annotations


def min_edits_to_substring(text: str, pattern: str) -> int:
    """Return the minimum edit distance between `pattern` and any substring of `text`.

    Edits are insertions, deletions, and substitutions (Levenshtein distance).
    The empty substring is allowed, so the answer is at most len(pattern).

    Suggested approach (Bitap as an oracle):
      1. Write a helper `occurs_within(text, pattern, k)` that runs the
         Wu-Manber Bitap with k+1 registers (init R[d] = (1 << d) - 1) and
         returns True iff the top bit of R[k] is ever set -- INCLUDING a check
         of the initial register state before consuming any text.
      2. Loop k = 0, 1, 2, ..., len(pattern) and return the first k for which
         `occurs_within` is True. Monotonicity guarantees this is the minimum.

    Args:
        text:    The text to search within (lowercase English letters).
        pattern: The pattern to fuzzily locate (lowercase English letters,
                 length <= 64).

    Returns:
        The minimum number of edits to turn `pattern` into some substring of
        `text`. Returns 0 iff `pattern` is an exact substring of `text`.

    Example:
        >>> min_edits_to_substring("the quikc brown", "quick")
        1
    """
    # TODO: implement using a bounded-edit Bitap oracle looped over k.
    pass


if __name__ == "__main__":
    print(min_edits_to_substring("the quikc brown", "quick"))  # expected: 1
    print(min_edits_to_substring("recieve", "receive"))        # expected: 2
    print(min_edits_to_substring("aabbcc", "xyz"))             # expected: 3
