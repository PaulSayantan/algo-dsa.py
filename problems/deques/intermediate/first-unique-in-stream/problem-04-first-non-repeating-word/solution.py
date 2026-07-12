"""First non-repeating word in a stream — return the per-step answers."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def firstUniqWords(self, words: List[str]) -> List[str]:
        # TODO: counts by word + a deque of candidates; front is the first unique
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqWords(["the", "day", "is", "the", "day"]))  # expected: ['the', 'the', 'the', 'day', 'is']
    print(sol.firstUniqWords(["a", "b", "a", "c", "b"]))  # expected: ['a', 'a', 'b', 'b', 'c']
    print(sol.firstUniqWords(["x", "x"]))  # expected: ['x', '']
    print(sol.firstUniqWords([]))  # expected: []
