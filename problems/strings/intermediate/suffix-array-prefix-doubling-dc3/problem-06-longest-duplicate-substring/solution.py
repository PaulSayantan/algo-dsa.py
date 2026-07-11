"""Longest Duplicate Substring (LeetCode 1044).

Return any longest substring that occurs at least twice in s (overlaps allowed),
or "" if none. Suffix array + LCP: the answer is the shared prefix at the adjacent
sorted-suffix pair with the maximum LCP.
"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """Return a longest duplicated substring of ``s``.

        Args:
            s: The input string of lowercase English letters.

        Returns:
            Any duplicated substring of maximum length; "" if no substring repeats.

        Example:
            >>> Solution().longestDupSubstring("banana")
            'ana'
        """
        # TODO: build the suffix array of s, compute the LCP array (Kasai),
        # find the index i with the largest lcp[i], and return
        #   s[sa[i] : sa[i] + lcp[i]]  (or "" if the max LCP is 0).
        pass


if __name__ == "__main__":
    print(Solution().longestDupSubstring("banana"))   # expected: "ana"
    print(Solution().longestDupSubstring("abcd"))       # expected: ""
    print(Solution().longestDupSubstring("aaaaa"))      # expected: "aaaa"
