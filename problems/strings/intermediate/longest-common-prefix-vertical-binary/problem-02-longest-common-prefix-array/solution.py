"""LeetCode 14 — Longest Common Prefix.

Fill in `Solution.longestCommonPrefix` so it returns the longest common prefix shared by
every string in `strs`.
"""
from __future__ import annotations

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Return the longest common prefix of all strings in `strs`.

        Args:
            strs: A non-empty list of strings.

        Returns:
            The longest string that is a prefix of every element of `strs`, or "" if the
            strings share no common leading character.

        Example:
            >>> Solution().longestCommonPrefix(["flower", "flow", "flight"])
            'fl'
            >>> Solution().longestCommonPrefix(["dog", "racecar", "car"])
            ''
        """
        # TODO: implement (vertical column scan, or binary search on prefix length)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))          # expected: "fl"
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))             # expected: ""
    print(sol.longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # expected: "inters"
    print(sol.longestCommonPrefix(["throne"]))                            # expected: "throne"
