"""Shortest Common Supersequence (LeetCode 1092).

Empty solution template — fill in the logic yourself.
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """Return the shortest string that has both str1 and str2 as subsequences.

        If multiple shortest supersequences exist, any one of them is acceptable.

        Args:
            str1: The first string.
            str2: The second string.

        Returns:
            A shortest string s such that str1 and str2 are both subsequences of s.

        Example:
            >>> Solution().shortestCommonSupersequence("abac", "cab")
            'cabac'
            >>> Solution().shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa")
            'aaaaaaaa'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    scs = sol.shortestCommonSupersequence("abac", "cab")
    # expected: a length-5 string such as "cabac" that contains both inputs as subsequences
    print(scs)
    print(sol.shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa"))  # expected: "aaaaaaaa"
