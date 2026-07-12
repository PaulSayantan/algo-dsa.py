"""Groups of Special-Equivalent Strings — LeetCode 893."""
from typing import List  # noqa: F401


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        # TODO: signature = (sorted even-index chars, sorted odd-index chars)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSpecialEquivGroups(["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]))  # expected: 3
    print(sol.numSpecialEquivGroups(["abc", "acb", "bac", "bca", "cab", "cba"]))  # expected: 3
