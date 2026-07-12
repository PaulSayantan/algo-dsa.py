"""Validate a prefix (Polish notation) expression by tracking operand arity."""


class Solution:
    def isValidPrefix(self, expr: str) -> bool:
        # TODO: scan right-to-left; push a marker per operand, pop two per operator
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValidPrefix("*+AB-CD"))  # expected: True
    print(sol.isValidPrefix("+A"))  # expected: False
    print(sol.isValidPrefix("AB"))  # expected: False
    print(sol.isValidPrefix("A"))  # expected: True
    print(sol.isValidPrefix(""))  # expected: False
