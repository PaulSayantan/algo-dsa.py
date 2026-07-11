"""Range modulo + point assignment + range sum (Codeforces 438D style).

Solve with a Segment Tree Beats-style break condition: store the range maximum
so a range-modulo update can prune any sub-range whose maximum is strictly less
than the modulus (those elements are unaffected). Every real reduction more than
halves the value, giving near-linear amortized total cost.

This file is an EMPTY TEMPLATE. Fill in the implementation yourself.
"""
from __future__ import annotations

from typing import List


class Solution:
    def processOperations(self, nums: List[int], ops: List[List[int]]) -> List[int]:
        """Process range-modulo, point-assignment, and sum operations.

        Args:
            nums: The initial array of ``n`` positive integers (treated as
                1-indexed by the operations, i.e. ``nums[0]`` is element ``1``).
            ops: A list of operations. Each operation is one of:
                ``[1, l, r]``      -> report the sum of ``nums[l..r]``;
                ``[2, l, r, x]``   -> set ``nums[i] = nums[i] % x`` for ``i`` in
                                      ``[l, r]``;
                ``[3, k, x]``      -> set ``nums[k] = x``.
                All indices are 1-indexed.

        Returns:
            A list with one entry per type-1 sum query, in the order the sum
            queries appear in ``ops``.

        Example:
            >>> Solution().processOperations(
            ...     [1, 2, 3, 4, 5],
            ...     [[2, 3, 5, 4], [3, 3, 5], [1, 2, 5]])
            [8]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # Expected: [8]
    print(sol.processOperations([1, 2, 3, 4, 5], [[2, 3, 5, 4], [3, 3, 5], [1, 2, 5]]))
    # Expected: [30, 9]
    print(sol.processOperations([10, 10, 10], [[1, 1, 3], [2, 1, 3, 7], [1, 1, 3]]))
