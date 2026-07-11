"""LeetCode 1649 - Create Sorted Array through Instructions.

Fill in the body using a Binary Indexed Tree (Fenwick Tree) over values,
querying counts of strictly-smaller and strictly-greater inserted elements.
"""

from typing import List


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        """Return the total insertion cost, modulo 1_000_000_007.

        The cost of inserting a value v is min(#already-inserted strictly less
        than v, #already-inserted strictly greater than v).

        Args:
            instructions: Values inserted one at a time, in the given order.

        Returns:
            Sum of all insertion costs modulo 1_000_000_007.

        Example:
            >>> Solution().createSortedArray([1, 5, 6, 2])
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.createSortedArray([1, 5, 6, 2]))                    # expected: 1
    print(sol.createSortedArray([1, 2, 3, 6, 5, 4]))              # expected: 3
    print(sol.createSortedArray([1, 3, 3, 3, 2, 4, 2, 1, 2]))     # expected: 4
