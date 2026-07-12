"""Convert a prefix (Polish notation) expression to infix."""


class Solution:
    def prefixToInfix(self, expr: str) -> str:
        # TODO: scan right-to-left; on an operator pop two operands and wrap in ( )
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.prefixToInfix("+AB"))  # expected: '(A+B)'
    print(sol.prefixToInfix("*+AB-CD"))  # expected: '((A+B)*(C-D))'
    print(sol.prefixToInfix("*-A/BC-/AKL"))  # expected: '((A-(B/C))*((A/K)-L))'
    print(sol.prefixToInfix("A"))  # expected: 'A'
