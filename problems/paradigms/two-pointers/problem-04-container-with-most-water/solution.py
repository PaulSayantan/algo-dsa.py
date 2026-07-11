from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Return the maximum water area between two of the vertical lines.

        The area formed by lines at indices ``i < j`` is
        ``min(height[i], height[j]) * (j - i)``.

        Args:
            height: A list of non-negative integer line heights, length >= 2.

        Returns:
            The largest achievable container area.

        Example:
            >>> Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
            49
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # expected: 49
    print(sol.maxArea([1, 1]))                        # expected: 1
    print(sol.maxArea([4, 3, 2, 1, 4]))               # expected: 16
