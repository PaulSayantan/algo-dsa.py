"""Find K Pairs with Smallest Sums (LeetCode 373).

Return the k pairs (one element from each sorted array) with the smallest sums. Do NOT
build all m*n pairs. Recommended: a min-heap over a moving frontier of candidate pairs.
"""

from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        """Return the k pairs with the smallest sums u + v.

        Args:
            nums1: First array, sorted in non-decreasing order.
            nums2: Second array, sorted in non-decreasing order.
            k: The number of smallest-sum pairs to return.

        Returns:
            A list of up to k pairs [u, v] (u from nums1, v from nums2), ordered by
            increasing sum. Fewer than k pairs are returned only if fewer than k exist.

        Example:
            kSmallestPairs([1, 7, 11], [2, 4, 6], 3) -> [[1, 2], [1, 4], [1, 6]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))  # expected: [[1,2],[1,4],[1,6]]
    print(sol.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))   # expected: [[1,1],[1,1]]
    print(sol.kSmallestPairs([1, 2], [3], 3))            # expected: [[1,3],[2,3]]
