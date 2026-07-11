"""Longest Substring with At Most K Distinct Characters — empty template.

Fill in the body of `lengthOfLongestSubstringKDistinct`. Do not hard-code answers.
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """Return the length of the longest substring with at most k distinct chars.

        Args:
            s: The input string.
            k: The maximum number of distinct characters allowed in the window.

        Returns:
            The length of the longest contiguous substring of `s` containing at
            most `k` distinct characters. Returns 0 when k == 0.

        Example:
            >>> Solution().lengthOfLongestSubstringKDistinct("eceba", 2)
            3
        """
        # TODO: implement using a variable-size sliding window
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))          # expected: 3
    print(sol.lengthOfLongestSubstringKDistinct("aa", 1))             # expected: 2
    print(sol.lengthOfLongestSubstringKDistinct("abcadcacacaca", 3))  # expected: 11
    print(sol.lengthOfLongestSubstringKDistinct("abc", 0))            # expected: 0
