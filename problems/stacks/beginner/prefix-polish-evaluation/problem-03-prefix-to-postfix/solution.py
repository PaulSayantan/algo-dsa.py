"""Convert a prefix (Polish notation) expression to postfix (Reverse Polish)."""


class Solution:
    def prefixToPostfix(self, expr: str) -> str:
        # TODO: scan right-to-left; on an operator pop two operands and append the operator
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.prefixToPostfix("+AB"))  # expected: 'AB+'
    print(sol.prefixToPostfix("*-AB/CD"))  # expected: 'AB-CD/*'
    print(sol.prefixToPostfix("*-A/BC-/AKL"))  # expected: 'ABC/-AK/L-*'
    print(sol.prefixToPostfix("A"))  # expected: 'A'
