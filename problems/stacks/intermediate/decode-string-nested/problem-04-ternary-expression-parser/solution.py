"""Ternary Expression Parser — LeetCode 439."""


class Solution:
    def parseTernary(self, expression: str) -> str:
        # TODO: scan right-to-left; when a condition sits before '?', fold the branch
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.parseTernary("T?2:3"))  # expected: '2'
    print(sol.parseTernary("F?1:T?4:5"))  # expected: '4'
    print(sol.parseTernary("T?T?F:5:3"))  # expected: 'F'
    print(sol.parseTernary("F?T:F"))  # expected: 'F'
