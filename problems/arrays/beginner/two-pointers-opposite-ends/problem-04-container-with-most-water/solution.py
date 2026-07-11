"""Container With Most Water — LeetCode 11.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Return the maximum water area between any two of the vertical lines.

        Args:
            height: A list where height[i] is the height of the i-th vertical
                line at x-coordinate i.

        Returns:
            The maximum value of min(height[i], height[j]) * (j - i) over all
            pairs i < j.

        Example:
            >>> Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
            49
        """
        # TODO: implement using two pointers (opposite ends)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # expected: 49
    print(sol.maxArea([1, 1]))                        # expected: 1
    print(sol.maxArea([4, 3, 2, 1, 4]))               # expected: 16
