"""Naive Operations: range increment + range sum of floor(a[i]/b[i]) (HDU 6315).

Solve with a Segment Tree Beats-style break condition on a per-index countdown.
Each leaf tracks need[i] = how many more increments until floor(a[i]/b[i]) rises
by 1 (starts at b[i]). A range increment is a lazy range -1 on the countdown;
tracking the range minimum lets you prune any sub-range whose minimum countdown
is still > 0. Only where the minimum hits 0 do you tick the answer and reset.

This file is an EMPTY TEMPLATE. Fill in the implementation yourself.
"""
from __future__ import annotations

from typing import List


class Solution:
    def naiveOperations(self, b: List[int], ops: List[List[int]]) -> List[int]:
        """Process range increments and range floor-division sum queries.

        Args:
            b: A fixed array of length ``n`` that is a permutation of ``1..n``
                (treated as 1-indexed by the operations). The array ``a`` starts
                as all zeros.
            ops: A list of operations. Each operation is one of:
                ``[0, l, r]`` -> ``a[i] += 1`` for every ``i`` in ``[l, r]``;
                ``[1, l, r]`` -> report ``sum of floor(a[i] / b[i])`` for ``i``
                                 in ``[l, r]``.
                All indices are 1-indexed.

        Returns:
            A list with one entry per type-1 query, in the order the queries
            appear in ``ops``.

        Example:
            >>> Solution().naiveOperations(
            ...     [2, 3],
            ...     [[0, 1, 2], [1, 1, 2], [0, 1, 1], [1, 1, 2]])
            [0, 1]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # Expected: [0, 1]
    print(sol.naiveOperations(
        [2, 3],
        [[0, 1, 2], [1, 1, 2], [0, 1, 1], [1, 1, 2]]))
    # Expected: [1, 5, 2]
    print(sol.naiveOperations(
        [1, 2, 3, 4, 5, 6],
        [[0, 1, 3], [1, 1, 4], [0, 1, 6], [0, 1, 3], [1, 1, 4], [1, 2, 5]]))
