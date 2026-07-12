"""Valid Parentheses — LeetCode 20."""


class Solution:
    def isValid(self, s: str) -> bool:
        # TODO: push openers onto a stack; on a closer, pop and match the head
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()[]{}"))  # expected: True
    print(sol.isValid("(]"))  # expected: False
    print(sol.isValid("([{}])"))  # expected: True
    print(sol.isValid("("))  # expected: False
