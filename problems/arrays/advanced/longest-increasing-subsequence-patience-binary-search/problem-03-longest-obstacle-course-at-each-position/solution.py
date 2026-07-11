"""Find the Longest Valid Obstacle Course at Each Position (LeetCode 1964).

Empty solution template — fill in the logic yourself.
"""
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """For each index i, return the length of the longest non-decreasing
        course ending at index i using obstacles[0..i].

        Args:
            obstacles: Heights of the obstacles in build order.

        Returns:
            A list ans where ans[i] is the length of the longest
            non-decreasing subsequence of obstacles[0..i] that ends at i.

        Example:
            >>> Solution().longestObstacleCourseAtEachPosition([1, 2, 3, 2])
            [1, 2, 3, 3]
            >>> Solution().longestObstacleCourseAtEachPosition([2, 2, 1])
            [1, 2, 1]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestObstacleCourseAtEachPosition([1, 2, 3, 2]))
    # expected: [1, 2, 3, 3]
    print(sol.longestObstacleCourseAtEachPosition([2, 2, 1]))
    # expected: [1, 2, 1]
    print(sol.longestObstacleCourseAtEachPosition([3, 1, 5, 6, 4, 2]))
    # expected: [1, 1, 2, 3, 2, 2]
