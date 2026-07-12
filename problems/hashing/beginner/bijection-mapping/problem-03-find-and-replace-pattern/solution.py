"""Find and Replace Pattern — LeetCode 890."""
from typing import List  # noqa: F401


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # TODO: normalize each word to its first-occurrence pattern and compare
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))  # expected: ['mee', 'aqq']
    print(sol.findAndReplacePattern(["a", "b", "c"], "a"))  # expected: ['a', 'b', 'c']
