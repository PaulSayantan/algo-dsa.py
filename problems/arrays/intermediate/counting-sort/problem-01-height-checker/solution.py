"""Height Checker — LeetCode 1051.

Count how many students are standing in a position that differs from the
non-decreasing sorted arrangement.
"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """Return the number of indices whose height differs from sorted order.

        Args:
            heights: Current left-to-right order of student heights. Each value
                is an integer in the range [1, 100].

        Returns:
            The count of indices ``i`` where ``heights[i]`` does not equal the
            value at index ``i`` of ``heights`` sorted in non-decreasing order.

        Example:
            >>> Solution().heightChecker([1, 1, 4, 2, 1, 3])
            3
        """
        # TODO: implement using Counting Sort (values are bounded by 100).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.heightChecker([1, 1, 4, 2, 1, 3]))  # expected: 3
    print(sol.heightChecker([5, 1, 2, 3, 4]))      # expected: 5
    print(sol.heightChecker([1, 2, 3, 4, 5]))      # expected: 0
