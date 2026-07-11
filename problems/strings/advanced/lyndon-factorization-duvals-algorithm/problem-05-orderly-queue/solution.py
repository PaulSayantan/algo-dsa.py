"""Orderly Queue (LeetCode 899).

Implement `Solution.orderlyQueue`. For k >= 2 the answer is the sorted string; for
k == 1 it is the lexicographically smallest rotation, which you should compute with
Duval's algorithm on s + s.
"""
from __future__ import annotations


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """Return the smallest string reachable by moving any of the first k chars to end.

        Args:
            s: A non-empty string of lowercase English letters.
            k: Number of leading positions from which a character may be moved (1 <= k <= len(s)).

        Returns:
            The lexicographically smallest reachable string.

        Example:
            >>> Solution().orderlyQueue("cba", 1)
            'acb'
            >>> Solution().orderlyQueue("baaca", 3)
            'aaabc'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.orderlyQueue("cba", 1))    # expected: 'acb'
    print(sol.orderlyQueue("baaca", 3))  # expected: 'aaabc'
    print(sol.orderlyQueue("dcba", 1))   # expected: 'adcb'
