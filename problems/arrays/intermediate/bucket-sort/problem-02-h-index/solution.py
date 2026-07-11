"""LeetCode 274 - H-Index.

Fill in the body of `hIndex` using Bucket Sort.
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """Compute the researcher's h-index.

        Args:
            citations: citations[i] is the citation count of the i-th paper.

        Returns:
            The maximum h such that at least h papers each have >= h citations.

        Example:
            >>> Solution().hIndex([3, 0, 6, 1, 5])
            3
        """
        # TODO: implement using bucket sort over capped citation counts
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.hIndex([3, 0, 6, 1, 5]))  # expected: 3
    print(sol.hIndex([1, 3, 1]))        # expected: 1
    print(sol.hIndex([0, 0]))           # expected: 0
