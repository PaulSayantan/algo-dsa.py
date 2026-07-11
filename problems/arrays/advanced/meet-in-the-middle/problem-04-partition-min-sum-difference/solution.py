"""Partition Array Into Two Arrays to Minimize Sum Difference
(LeetCode 2035) — empty solution template.

Fill in `Solution.minimumDifference` using the Meet in the Middle technique.
"""

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """Minimize |sum(A) - sum(B)| when splitting nums into two size-n arrays.

        Args:
            nums: A list of exactly 2 * n integers (1 <= n <= 15), possibly
                negative, zero, or positive.

        Returns:
            The minimum achievable absolute difference between the sums of the two
            length-n parts.

        Example:
            >>> Solution().minimumDifference([3, 9, 7, 3])
            2
            >>> Solution().minimumDifference([2, -1, 0, 4, -2, -9])
            0
        """
        # TODO: implement using Meet in the Middle
        pass


if __name__ == "__main__":
    print(Solution().minimumDifference([3, 9, 7, 3]))              # expected: 2
    print(Solution().minimumDifference([-36, 36]))                 # expected: 72
    print(Solution().minimumDifference([2, -1, 0, 4, -2, -9]))     # expected: 0
