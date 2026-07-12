"""Valid Parentheses. Use a stack to match brackets in LIFO order."""


class Solution:
    def isValid(self, s: str) -> bool:
        # TODO: push opens; on a close, pop and verify the pair matches
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))  # expected: True
    print(sol.isValid("()[]{}"))  # expected: True
    print(sol.isValid("(]"))  # expected: False
    print(sol.isValid("([)]"))  # expected: False
    print(sol.isValid("{[]}"))  # expected: True
    print(sol.isValid(""))  # expected: True
