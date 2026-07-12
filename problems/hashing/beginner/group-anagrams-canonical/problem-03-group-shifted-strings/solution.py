"""Group Shifted Strings — LeetCode 249."""
from collections import defaultdict  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # TODO: signature = gaps between consecutive letters, modulo 26
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))  # expected: [['a', 'z'], ['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba']]
    print(sol.groupStrings(["az", "ba", "a", "z"]))  # expected: [['a', 'z'], ['az', 'ba']]
