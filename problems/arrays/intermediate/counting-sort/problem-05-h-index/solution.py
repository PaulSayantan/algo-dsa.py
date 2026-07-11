"""H-Index — LeetCode 274.

Compute a researcher's h-index from their per-paper citation counts.
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """Return the h-index for the given citation counts.

        The h-index is the largest value ``h`` such that at least ``h`` papers
        each have at least ``h`` citations.

        Args:
            citations: Citation count of each paper. ``citations[i]`` is an
                integer in the range [0, 1000]; the list has 1..5000 entries.

        Returns:
            The researcher's h-index as a non-negative integer.

        Example:
            >>> Solution().hIndex([3, 0, 6, 1, 5])
            3
        """
        # TODO: implement using Counting Sort with counts capped at n.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.hIndex([3, 0, 6, 1, 5]))  # expected: 3
    print(sol.hIndex([1, 3, 1]))        # expected: 1
    print(sol.hIndex([0, 0]))           # expected: 0
