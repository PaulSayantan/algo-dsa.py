"""Permutation in String — LeetCode 567."""
from collections import Counter  # noqa: F401


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # TODO: fixed-size window over s2; True when its freq map equals Counter(s1)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))  # expected: True
    print(sol.checkInclusion("ab", "eidboaoo"))  # expected: False
    print(sol.checkInclusion("adc", "dcda"))  # expected: True
    print(sol.checkInclusion("a", ""))  # expected: False
