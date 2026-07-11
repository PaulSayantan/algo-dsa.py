"""Count Distinct Substrings (LeetCode 1698).

Count the number of distinct non-empty substrings of ``s`` by hashing every
substring in O(1) via prefix hashes and deduplicating with a set.
"""


class Solution:
    def countDistinct(self, s: str) -> int:
        """Return the number of distinct non-empty substrings of ``s``.

        Args:
            s: The input string (lowercase English letters).

        Returns:
            The count of unique substrings. Identical strings occurring at
            different positions are counted only once.

        Example:
            >>> Solution().countDistinct("aba")
            5
            >>> Solution().countDistinct("aaa")
            3
        """
        # TODO: implement with polynomial prefix hashing + a set.
        #   1. Build prefix hashes (ideally two channels / double hashing).
        #   2. For every (l, r), compute the O(1) substring hash and add it to a
        #      set; return len(set). Optionally group by length to bound
        #      collision risk, or store the double-hash tuple.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countDistinct("aba"))  # expected: 5
    print(sol.countDistinct("aaa"))  # expected: 3
    print(sol.countDistinct("abc"))  # expected: 6
