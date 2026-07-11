"""Full Segment Tree Beats: range chmin + chmax + add + range sum.

Each node maintains both ends of its value distribution -- max / strict
second-max / count-of-max (for chmin) and min / strict second-min / count-of-min
(for chmax) -- plus the sum and an add lazy tag. chmin/chmax apply as O(1) tags
when the target lies strictly between an extreme and its second extreme, and
otherwise recurse (the Beats "break"). Amortized O((n + q) log^2 n).

This file is an EMPTY TEMPLATE. Fill in the implementation yourself.
"""
from __future__ import annotations

from typing import List


class Solution:
    def rangeChminChmaxAddSum(self, nums: List[int], ops: List[List[int]]) -> List[int]:
        """Process chmin, chmax, add updates and range-sum queries.

        Args:
            nums: The initial array of ``n`` integers (0-indexed).
            ops: A list of operations, each over a half-open range ``[l, r)``:
                ``[0, l, r, x]`` -> ``nums[i] = min(nums[i], x)``;
                ``[1, l, r, x]`` -> ``nums[i] = max(nums[i], x)``;
                ``[2, l, r, x]`` -> ``nums[i] += x`` (``x`` may be negative);
                ``[3, l, r]``    -> report ``sum of nums[i]`` for ``i`` in ``[l, r)``.
                Indices are 0-indexed with ``0 <= l < r <= n``.

        Returns:
            A list with one entry per type-3 sum query, in the order the sum
            queries appear in ``ops``.

        Example:
            >>> Solution().rangeChminChmaxAddSum(
            ...     [1, 2, 3, 4, 5],
            ...     [[3, 0, 5], [0, 0, 5, 3], [3, 0, 5], [2, 0, 5, 2], [3, 0, 5]])
            [15, 12, 22]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # Expected: [15, 12, 22]
    print(sol.rangeChminChmaxAddSum(
        [1, 2, 3, 4, 5],
        [[3, 0, 5], [0, 0, 5, 3], [3, 0, 5], [2, 0, 5, 2], [3, 0, 5]]))
    # Expected: [5, 2]
    print(sol.rangeChminChmaxAddSum(
        [-3, 0, 4, 1],
        [[1, 0, 4, 0], [3, 0, 4], [0, 1, 3, 1], [3, 0, 4]]))
