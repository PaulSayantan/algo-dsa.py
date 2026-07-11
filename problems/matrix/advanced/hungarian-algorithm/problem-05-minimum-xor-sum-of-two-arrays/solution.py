"""Minimum XOR Sum of Two Arrays (LeetCode 1879) — empty solution template.

Model as an assignment problem with cost[i][j] = nums1[i] ^ nums2[j] and run the
Hungarian Algorithm to find the minimum-cost perfect matching. Do NOT hard-code
answers.
"""

from typing import List


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        """Return the minimum XOR sum after optimally rearranging ``nums2``.

        Args:
            nums1: Integer array of length ``n``.
            nums2: Integer array of length ``n``; may be permuted freely.

        Returns:
            The minimum achievable value of
            ``sum(nums1[i] ^ perm2[i] for i in range(n))`` over all permutations
            ``perm2`` of ``nums2``.

        Example:
            >>> Solution().minimumXORSum([1, 2], [2, 3])
            2
        """
        # TODO: implement.
        #   1) cost[i][j] = nums1[i] ^ nums2[j]
        #   2) run Hungarian on the n x n cost matrix
        #   3) return the minimum total cost
        pass


if __name__ == "__main__":
    print(Solution().minimumXORSum([1, 2], [2, 3]))        # Expected: 2
    print(Solution().minimumXORSum([1, 0, 3], [5, 3, 4]))  # Expected: 8
