"""Group Shifted Strings — LeetCode 249.

Group strings that belong to the same shifting sequence by bucketing them under
a consecutive-difference hashing signature.
"""

from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """Group strings that are shifts of one another.

        A string ``t`` is a shift of ``s`` if adding a fixed amount (mod 26) to
        every character of ``s`` yields ``t``. Strings in the same shifting
        sequence must land in the same group.

        Args:
            strings: A list of lowercase-letter strings.

        Returns:
            A list of groups, where each group contains all strings sharing a
            single shifting sequence. Groups may be returned in any order.

        Example:
            >>> Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
            [['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']]  # order may vary
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
    # expected (any order):
    #   [["abc","bcd","xyz"], ["acef"], ["az","ba"], ["a","z"]]
    print(sol.groupStrings(["a", "b", "c"]))          # expected: [["a","b","c"]]
    print(sol.groupStrings(["abc", "cde", "fgh"]))    # expected: [["abc","cde","fgh"]]
