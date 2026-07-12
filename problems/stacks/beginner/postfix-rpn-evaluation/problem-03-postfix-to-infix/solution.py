"""Postfix to Infix Conversion — classic RPN stack exercise."""


class Solution:
    def postfixToInfix(self, expression: str) -> str:
        # TODO: use a stack of infix strings; on an operator pop b then a and push "(a op b)"
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.postfixToInfix("ab+"))  # expected: '(a+b)'
    print(sol.postfixToInfix("ab*c+"))  # expected: '((a*b)+c)'
    print(sol.postfixToInfix("abc*+"))  # expected: '(a+(b*c))'
    print(sol.postfixToInfix("wx-yz-/"))  # expected: '((w-x)/(y-z))'
    print(sol.postfixToInfix("a"))  # expected: 'a'
