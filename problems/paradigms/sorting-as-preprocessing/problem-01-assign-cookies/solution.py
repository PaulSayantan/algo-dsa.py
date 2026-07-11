"""Assign Cookies — LeetCode 455.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """Return the maximum number of content children.

        A child i (greed factor g[i]) is content if it receives a cookie j with
        s[j] >= g[i]. Each child gets at most one cookie and each cookie is used
        at most once.

        Args:
            g: Greed factors of the children (minimum acceptable cookie size).
            s: Sizes of the available cookies.

        Returns:
            The maximum number of children that can be made content.

        Example:
            >>> Solution().findContentChildren([1, 2, 3], [1, 1])
            1
            >>> Solution().findContentChildren([1, 2], [1, 2, 3])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findContentChildren([1, 2, 3], [1, 1]))      # expected: 1
    print(sol.findContentChildren([1, 2], [1, 2, 3]))      # expected: 2
    print(sol.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))  # expected: 2
