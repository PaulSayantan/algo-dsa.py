"""Group Anagrams — LeetCode 49."""
from collections import defaultdict  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # TODO: map the sorted-letters signature -> list of words
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # expected: [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
    print(sol.groupAnagrams([""]))  # expected: [['']]
    print(sol.groupAnagrams(["a"]))  # expected: [['a']]
