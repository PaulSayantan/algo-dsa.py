"""Evaluate a boolean prefix (Polish notation) expression."""


class Solution:
    def evalBoolPrefix(self, expr: str) -> bool:
        # TODO: scan right-to-left with a stack; T/F are operands, & and | are operators
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.evalBoolPrefix("&T|FT"))  # expected: True
    print(sol.evalBoolPrefix("|F&FT"))  # expected: False
    print(sol.evalBoolPrefix("&|TF&TT"))  # expected: True
    print(sol.evalBoolPrefix("T"))  # expected: True
