"""Sort Characters By Frequency — Selection Sort on a derived key (LeetCode 451).

Return `s` reordered so characters appear grouped in decreasing frequency.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        """Reorder a string so characters are grouped by descending frequency.

        Args:
            s: The input string of letters and digits.

        Returns:
            A permutation of `s` in which characters are grouped together and
            groups are ordered from most frequent to least frequent. Ties may
            be broken arbitrarily.

        Example:
            >>> Solution().frequencySort("tree") in {"eert", "eetr"}
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.frequencySort("tree"))     # expected: "eert" (or "eetr")
    print(sol.frequencySort("cccaaa"))   # expected: "aaaccc" (or "cccaaa")
    print(sol.frequencySort("Aabb"))     # expected: "bbAa" (or "bbaA")
