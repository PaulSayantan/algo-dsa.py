"""Minimum Insertions to Balance a Parentheses String — LeetCode 1541."""


class Solution:
    def minInsertions(self, s: str) -> int:
        # TODO: track owed ')' (2 per '('); count forced insertions, add leftover
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minInsertions("(()))"))  # expected: 1
    print(sol.minInsertions("())"))  # expected: 0
    print(sol.minInsertions("))())("))  # expected: 3
    print(sol.minInsertions("(("))  # expected: 4
    print(sol.minInsertions("()"))  # expected: 1
    print(sol.minInsertions(""))  # expected: 0
