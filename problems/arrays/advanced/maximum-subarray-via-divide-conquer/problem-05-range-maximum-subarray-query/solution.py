"""Range Maximum Subarray Query (SPOJ GSS1) — segment-tree template.

Build a segment tree whose every node stores the divide & conquer range summary
(total, best_prefix, best_suffix, best). The merge of two children is EXACTLY the
crossing-combine rule of the one-shot max-subarray algorithm:

    total       = L.total + R.total
    best_prefix = max(L.best_prefix, L.total + R.best_prefix)
    best_suffix = max(R.best_suffix, R.total + L.best_suffix)
    best        = max(L.best, R.best, L.best_suffix + R.best_prefix)

Build in O(n); answer each (l, r) query by merging O(log n) node summaries.
"""
from typing import List, Tuple


class Solution:
    def rangeMaxSubarray(
        self, nums: List[int], queries: List[Tuple[int, int]]
    ) -> List[int]:
        """Answer maximum-subarray-sum queries over sub-ranges of ``nums``.

        Args:
            nums: The base array of integers (values may be negative).
            queries: A list of ``(l, r)`` pairs, 0-based inclusive, with l <= r.

        Returns:
            A list of answers, one per query: the maximum sum of any non-empty
            contiguous subarray lying entirely within ``nums[l..r]``.

        Example:
            >>> Solution().rangeMaxSubarray([-1, 2, 3, -5, 4], [(0, 4), (3, 4)])
            [5, 4]
        """
        # TODO: implement using Maximum Subarray via Divide & Conquer
        # (build a segment tree of (total, best_prefix, best_suffix, best) nodes)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rangeMaxSubarray([-1, 2, 3, -5, 4], [(0, 4), (0, 2), (3, 4)]))  # expected: [5, 5, 4]
    print(sol.rangeMaxSubarray([-2, -3, -1, -4], [(0, 3), (1, 2)]))            # expected: [-1, -1]
    print(sol.rangeMaxSubarray([1, 2, 3, 4], [(0, 3), (2, 3)]))                # expected: [10, 7]
