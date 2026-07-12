"""Rearrange String k Distance Apart — LeetCode 358."""
import heapq  # noqa: F401
from collections import Counter, deque  # noqa: F401


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # TODO: max-heap by frequency + FIFO cooldown queue of length k
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rearrangeString("aabbcc", 3))  # expected: 'abcabc'
    print(sol.rearrangeString("aaabc", 3))  # expected: ''
    print(sol.rearrangeString("aaadbbcc", 2))  # expected: 'abacabcd'
    print(sol.rearrangeString("aaa", 0))  # expected: 'aaa'
