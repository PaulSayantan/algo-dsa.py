"""Group Anagrams — empty solution template.

Fill in the body of `groupAnagrams` using a hash map keyed by a canonical form.
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Group strings that are anagrams of one another.

        Args:
            strs: List of lowercase strings (an empty string is allowed).

        Returns:
            A list of groups, where each group is a list of strings that are all
            anagrams of each other. Group order and within-group order are
            unspecified.

        Example:
            >>> Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # expected (order may vary): [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(sol.groupAnagrams([""]))   # expected: [['']]
    print(sol.groupAnagrams(["a"]))  # expected: [['a']]
