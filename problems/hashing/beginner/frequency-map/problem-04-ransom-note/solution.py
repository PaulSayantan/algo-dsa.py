"""Ransom Note — LeetCode 383."""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # TODO: the magazine must contain at least as many of each letter as the note
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("a", "b"))  # expected: False
    print(sol.canConstruct("aa", "ab"))  # expected: False
    print(sol.canConstruct("aa", "aab"))  # expected: True
    print(sol.canConstruct("abc", "aabbcc"))  # expected: True
