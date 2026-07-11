"""LeetCode 451 - Sort Characters By Frequency.

Reorder the string so characters appear in decreasing order of frequency.
Fill in the body using a Character Frequency Count.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        """Return s reordered so more frequent characters come first.

        Characters that tie on frequency may appear in any relative order, but all
        occurrences of the same character must be grouped contiguously.

        Args:
            s: A string of uppercase/lowercase English letters and digits.

        Returns:
            A permutation of s sorted by descending character frequency.

        Example:
            >>> Solution().frequencySort("tree") in {"eert", "eetr"}
            True
            >>> sorted(Solution().frequencySort("cccaaa")) == sorted("cccaaa")
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.frequencySort("tree"))    # expected: "eert" (or "eetr")
    print(sol.frequencySort("cccaaa"))  # expected: "aaaccc" (or "cccaaa")
    print(sol.frequencySort("Aabb"))    # expected: "bbAa" (or "bbaA")
