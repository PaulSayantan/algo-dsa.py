"""Basic Calculator — LeetCode 224."""


class Solution:
    def calculate(self, s: str) -> int:
        # TODO: stack of (result, sign) across parentheses
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate("1 + 1"))  # expected: 2
    print(sol.calculate(" 2-1 + 2 "))  # expected: 3
    print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))  # expected: 23
    print(sol.calculate("- (3 + (4 - 1))"))  # expected: -6
