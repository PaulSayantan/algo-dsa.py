"""Gorgeous Sequence: range chmin + range max + range sum (HDU 5306).

Solve with Segment Tree Beats. Each node stores: max value, count of the max,
strict second max, and sum. A chmin(x) on a node is: a no-op if x >= max; an
O(1) tag if secondMax < x < max (lower only the maxima); otherwise recurse into
children ("the tree gets beaten"). Amortized O((n + q) log n).

This file is an EMPTY TEMPLATE. Fill in the implementation yourself.
"""
from __future__ import annotations

from typing import List


class Solution:
    def gorgeousSequence(self, nums: List[int], ops: List[List[int]]) -> List[int]:
        """Process range-chmin updates and range max/sum queries.

        Args:
            nums: The initial array of ``n`` non-negative integers (0-indexed).
            ops: A list of operations. Each operation is one of:
                ``[0, l, r, x]`` -> set ``nums[i] = min(nums[i], x)`` for ``i``
                                    in the inclusive range ``[l, r]``;
                ``[1, l, r]``    -> report the maximum of ``nums[l..r]``;
                ``[2, l, r]``    -> report the sum of ``nums[l..r]``.
                All indices are 0-indexed.

        Returns:
            A list with one entry per query operation (types 1 and 2), in the
            order those queries appear in ``ops``.

        Example:
            >>> Solution().gorgeousSequence(
            ...     [5, 4, 3, 2, 1],
            ...     [[1, 0, 4], [0, 0, 4, 3], [2, 0, 4], [1, 0, 4]])
            [5, 12, 3]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # Expected: [5, 12, 3]
    print(sol.gorgeousSequence(
        [5, 4, 3, 2, 1],
        [[1, 0, 4], [0, 0, 4, 3], [2, 0, 4], [1, 0, 4]]))
    # Expected: [18, 4]
    print(sol.gorgeousSequence(
        [1, 7, 7, 7, 5],
        [[0, 1, 3, 4], [2, 0, 4], [1, 1, 3]]))
