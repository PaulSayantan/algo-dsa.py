"""Longest Common Binary Prefix.

Fill in `longest_common_binary_prefix` so it returns the number of leading bits shared by
every value when each is written as a `width`-bit, left-zero-padded binary string.
"""
from __future__ import annotations

from typing import List


def longest_common_binary_prefix(nums: List[int], width: int) -> int:
    """Return the length of the longest common prefix of the fixed-width binary codes.

    Args:
        nums: A non-empty list of non-negative integers, each < 2**width.
        width: The number of bits used to represent each value (most significant first).

    Returns:
        The count of leading bits (from the most significant bit) on which every value in
        `nums` agrees. A value in the range [0, width].

    Example:
        >>> longest_common_binary_prefix([12, 13], 8)
        7
        >>> longest_common_binary_prefix([0, 15], 4)
        0
    """
    # TODO: implement
    #   Option A: format each value as format(v, f"0{width}b") and vertical-scan columns.
    #   Option B: binary search on the prefix length.
    #   Option C: use the highest differing bit of (max ^ min).
    pass


if __name__ == "__main__":
    print(longest_common_binary_prefix([12, 13], 8))    # expected: 7
    print(longest_common_binary_prefix([8, 8, 8], 4))   # expected: 4
    print(longest_common_binary_prefix([5, 6, 7], 4))   # expected: 2
    print(longest_common_binary_prefix([0, 15], 4))     # expected: 0
