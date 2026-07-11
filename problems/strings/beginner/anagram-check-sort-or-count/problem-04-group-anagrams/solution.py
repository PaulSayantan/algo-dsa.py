"""LeetCode 49 - Group Anagrams.

Fill in the body of `groupAnagrams`. Do not change the signature.
"""

from collections import defaultdict  # noqa: F401  (available if you choose to use it)
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Group strings that are anagrams of one another.

        Args:
            strs: A list of lowercase strings (the empty string is allowed).

        Returns:
            A list of groups, where each group contains all input strings that are
            anagrams of each other. Groups and the members within them may be in any
            order.

        Example:
            >>> groups = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
            >>> sorted(sorted(g) for g in groups)
            [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # expected (in some order): [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(sol.groupAnagrams([""]))   # expected: [[""]]
    print(sol.groupAnagrams(["a"]))  # expected: [["a"]]
