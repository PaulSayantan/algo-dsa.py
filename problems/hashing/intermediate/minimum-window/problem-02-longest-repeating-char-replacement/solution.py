"""Longest Repeating Character Replacement — LeetCode 424."""
from collections import defaultdict  # noqa: F401


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # TODO: window is valid while (len - max_freq) <= k; track the longest
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))  # expected: 4
    print(sol.characterReplacement("AABABBA", 1))  # expected: 4
    print(sol.characterReplacement("AAAA", 0))  # expected: 4
    print(sol.characterReplacement("ABCDE", 1))  # expected: 2
