"""Valid Parentheses — LeetCode 20."""


class Solution:
    def isValid(self, s: str) -> bool:
        # TODO: use a stack of open brackets
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))  # expected: True
    print(sol.isValid("()[]{}"))  # expected: True
    print(sol.isValid("(]"))  # expected: False
    print(sol.isValid("([)]"))  # expected: False
    print(sol.isValid("{[]}"))  # expected: True
    print(sol.isValid("("))  # expected: False
