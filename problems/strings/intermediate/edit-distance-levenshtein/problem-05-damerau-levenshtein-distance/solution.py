"""Damerau-Levenshtein Distance (Optimal String Alignment variant).

Compute the minimum number of insert / delete / replace / adjacent-transpose
operations to transform one string into another.
"""


class Solution:
    def damerauLevenshtein(self, a: str, b: str) -> int:
        """Return the Optimal String Alignment Damerau-Levenshtein distance.

        Allowed operations, each costing one step: insert a character, delete a
        character, replace a character, or transpose two adjacent characters.
        Uses the OSA restriction: no substring is edited more than once.

        Args:
            a: The source string to transform.
            b: The target string to reach.

        Returns:
            The minimum number of insert, delete, replace, and adjacent
            transposition operations required to turn a into b.

        Example:
            >>> Solution().damerauLevenshtein("ca", "ac")
            1
            >>> Solution().damerauLevenshtein("teh", "the")
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.damerauLevenshtein("ca", "ac"))        # expected: 1
    print(sol.damerauLevenshtein("teh", "the"))      # expected: 1
    print(sol.damerauLevenshtein("sitting", "kitten"))  # expected: 3
    print(sol.damerauLevenshtein("abc", "abc"))      # expected: 0
