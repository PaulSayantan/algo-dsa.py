"""Longest Valid Parentheses — LeetCode 32."""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # TODO: stack of indices with a -1 base
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestValidParentheses("(()"))  # expected: 2
    print(sol.longestValidParentheses(")()())"))  # expected: 4
    print(sol.longestValidParentheses(""))  # expected: 0
    print(sol.longestValidParentheses("()(()"))  # expected: 2
