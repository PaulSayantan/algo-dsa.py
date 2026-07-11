"""Count Distinct Substrings.

Count the number of distinct non-empty substrings of `s`.
"""


class Solution:
    def countDistinctSubstrings(self, s: str) -> int:
        """Return the number of distinct non-empty substrings of `s`.

        Args:
            s: The input string of lowercase English letters.

        Returns:
            The count of distinct non-empty substrings.

        Example:
            >>> Solution().countDistinctSubstrings("banana")
            15
        """
        # TODO: implement
        #   1. Append a unique terminal and build a suffix tree (Ukkonen, O(n)).
        #   2. Sum the label length of every edge in the tree.
        #   3. Subtract the contribution of the terminal sentinel: exclude the
        #      one terminal character that sits on each leaf edge (equivalently,
        #      build over s + terminal and do not count the terminal character).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countDistinctSubstrings("banana"))  # expected: 15
    print(sol.countDistinctSubstrings("aaa"))      # expected: 3
    print(sol.countDistinctSubstrings("abc"))      # expected: 6
