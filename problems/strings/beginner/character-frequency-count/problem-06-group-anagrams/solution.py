"""LeetCode 49 - Group Anagrams.

Group strings that are anagrams of one another. Fill in the body using a
Character Frequency Count as each word's grouping key.
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Group the input strings so that anagrams land in the same list.

        Args:
            strs: A list of lowercase strings.

        Returns:
            A list of groups, where each group contains strings that are anagrams
            of each other. The order of the groups and of strings within a group
            does not matter.

        Example:
            >>> groups = Solution().groupAnagrams(["eat", "tea", "tan", "ate",
            ...                                     "nat", "bat"])
            >>> sorted(sorted(g) for g in groups)
            [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # expected (in any order): [["bat"], ["nat","tan"], ["ate","eat","tea"]]
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(sol.groupAnagrams([""]))   # expected: [[""]]
    print(sol.groupAnagrams(["a"]))  # expected: [["a"]]
