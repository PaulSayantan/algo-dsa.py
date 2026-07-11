"""Handling Sum Queries After Update (LeetCode 2569).

Fill in the segment-tree-with-lazy-propagation logic. Keep the LeetCode-style
signature below unchanged.
"""
from typing import List


class Solution:
    def handleQuery(
        self,
        nums1: List[int],
        nums2: List[int],
        queries: List[List[int]],
    ) -> List[int]:
        """Answer all type-3 (sum of nums2) queries in order.

        Args:
            nums1: Binary array (each element is 0 or 1).
            nums2: Integer array of the same length as nums1.
            queries: Each query is [type, a, b]:
                [1, l, r] -> flip nums1[l..r];
                [2, p, 0] -> nums2[i] += nums1[i] * p for all i;
                [3, 0, 0] -> record sum(nums2).

        Returns:
            The answers to the type-3 queries, in the order they appear.

        Example:
            Solution().handleQuery([1,0,1], [0,0,0], [[1,1,1],[2,1,0],[3,0,0]])
            # -> [3]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.handleQuery([1, 0, 1], [0, 0, 0], [[1, 1, 1], [2, 1, 0], [3, 0, 0]]))
    # expected: [3]
    print(sol.handleQuery([1], [5], [[2, 0, 0], [3, 0, 0]]))
    # expected: [5]
