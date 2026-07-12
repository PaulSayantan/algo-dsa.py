"""Postfix to Prefix Conversion — classic RPN stack exercise."""


class Solution:
    def postfixToPrefix(self, expression: str) -> str:
        # TODO: use a stack of strings; on an operator pop b then a and push op + a + b
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.postfixToPrefix("ab+"))  # expected: '+ab'
    print(sol.postfixToPrefix("ab+cd-*"))  # expected: '*+ab-cd'
    print(sol.postfixToPrefix("abc*+"))  # expected: '+a*bc'
    print(sol.postfixToPrefix("ab*c+d-"))  # expected: '-+*abcd'
    print(sol.postfixToPrefix("z"))  # expected: 'z'
