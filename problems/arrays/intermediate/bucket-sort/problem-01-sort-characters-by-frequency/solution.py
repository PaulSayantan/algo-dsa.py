"""LeetCode 451 - Sort Characters By Frequency.

Fill in the body of `frequencySort` using Bucket Sort.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        """Sort the characters of ``s`` in decreasing order of frequency.

        Args:
            s: The input string of letters and digits.

        Returns:
            A string containing the same characters as ``s`` but ordered so
            that more frequent characters come first. Characters that share a
            frequency may appear in any relative order.

        Example:
            >>> Solution().frequencySort("tree") in ("eert", "eetr")
            True
        """
        # TODO: implement using bucket sort by frequency
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.frequencySort("tree"))     # expected: "eert" or "eetr"
    print(sol.frequencySort("cccaaa"))   # expected: "aaaccc" or "cccaaa"
    print(sol.frequencySort("Aabb"))     # expected: "bbAa" or "bbaA"
