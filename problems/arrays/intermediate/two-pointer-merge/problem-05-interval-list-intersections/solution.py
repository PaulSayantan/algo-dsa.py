"""LeetCode 986 - Interval List Intersections.

Both interval lists are sorted by start. Use the Two-Pointer Merge technique,
advancing the interval that ends first. Fill in `intervalIntersection`.
"""

from typing import List


class Solution:
    def intervalIntersection(
        self,
        firstList: List[List[int]],
        secondList: List[List[int]],
    ) -> List[List[int]]:
        """Return the intersection of two sorted, disjoint closed-interval lists.

        Args:
            firstList: Sorted, pairwise-disjoint closed intervals [start, end].
            secondList: Sorted, pairwise-disjoint closed intervals [start, end].

        Returns:
            A list of closed intervals covered by both inputs, sorted by start.

        Example:
            >>> Solution().intervalIntersection([[1, 7]], [[3, 10]])
            [[3, 7]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()

    print(
        s.intervalIntersection(
            [[0, 2], [5, 10], [13, 23], [24, 25]],
            [[1, 5], [8, 12], [15, 24], [25, 26]],
        )
    )
    # expected: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    print(s.intervalIntersection([[1, 3], [5, 9]], []))  # expected: []

    print(s.intervalIntersection([[1, 7]], [[3, 10]]))   # expected: [[3, 7]]
