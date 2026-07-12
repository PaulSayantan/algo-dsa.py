"""Longest Substring with At Most K Distinct Characters — LeetCode 340."""
from collections import defaultdict  # noqa: F401


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # TODO: variable window; shrink while distinct-char count exceeds k
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))  # expected: 3
    print(sol.lengthOfLongestSubstringKDistinct("WORLD", 4))  # expected: 4
    print(sol.lengthOfLongestSubstringKDistinct("aaabbbccc", 2))  # expected: 6
    print(sol.lengthOfLongestSubstringKDistinct("a", 0))  # expected: 0
