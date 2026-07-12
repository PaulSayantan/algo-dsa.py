"""Valid Anagram — LeetCode 242."""
from collections import Counter  # noqa: F401


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # TODO: compare character frequency maps
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # expected: True
    print(sol.isAnagram("rat", "car"))  # expected: False
    print(sol.isAnagram("a", "ab"))  # expected: False
