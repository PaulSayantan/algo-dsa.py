"""Group Anagrams — LeetCode 49.

Group strings that are anagrams of one another by bucketing each string under a
canonical hashing signature.
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Group the anagrams in ``strs`` together.

        Args:
            strs: A list of lowercase-letter strings (some possibly empty).

        Returns:
            A list of groups, where each group is a list of strings that are all
            anagrams of one another. Groups and the strings within them may be
            returned in any order.

        Example:
            >>> Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]  # order may vary
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # expected (any order): [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    print(sol.groupAnagrams([""]))   # expected: [[""]]
    print(sol.groupAnagrams(["a"]))  # expected: [["a"]]
