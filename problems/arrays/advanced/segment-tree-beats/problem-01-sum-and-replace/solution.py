"""Range square-root update + range sum query.

Solve with a Segment Tree Beats-style break condition: store the range maximum
so a square-root update can prune any sub-range whose values are already stable
(max <= 1), giving near-linear amortized total cost.

This file is an EMPTY TEMPLATE. Fill in the implementation yourself.
"""
from __future__ import annotations

from typing import List


class Solution:
    def rangeSqrtSum(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """Process square-root updates and sum queries over an array.

        Args:
            nums: The initial array of ``n`` non-negative integers (treated as
                1-indexed by the queries, i.e. ``nums[0]`` is element ``1``).
            queries: A list of operations. Each operation is one of:
                ``[1, l, r]`` -> replace ``nums[i]`` with ``floor(sqrt(nums[i]))``
                for every ``i`` in the inclusive range ``[l, r]``;
                ``[2, l, r]`` -> report the sum of ``nums[i]`` over ``[l, r]``.
                Indices ``l`` and ``r`` are 1-indexed.

        Returns:
            A list with one entry per ``[2, l, r]`` sum query, in the order the
            sum queries appear in ``queries``.

        Example:
            >>> Solution().rangeSqrtSum([1, 4, 9, 16, 25],
            ...                         [[2, 1, 5], [1, 1, 5], [2, 1, 5]])
            [55, 15]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # Expected: [55, 15]
    print(sol.rangeSqrtSum([1, 4, 9, 16, 25], [[2, 1, 5], [1, 1, 5], [2, 1, 5]]))
    # Expected: [4, 3]
    print(sol.rangeSqrtSum([2, 3, 8], [[1, 1, 3], [2, 1, 3], [1, 1, 3], [2, 1, 3]]))
