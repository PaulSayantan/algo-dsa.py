"""Evaluate Boolean Postfix Expression — classic RPN stack exercise."""


class Solution:
    def evalBoolPostfix(self, tokens: str) -> bool:
        # TODO: stack of booleans; '&'/'|' pop two, unary '!' pops one
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.evalBoolPostfix("TF&"))  # expected: False
    print(sol.evalBoolPostfix("TF|"))  # expected: True
    print(sol.evalBoolPostfix("TF|!"))  # expected: False
    print(sol.evalBoolPostfix("TT&F|"))  # expected: True
    print(sol.evalBoolPostfix("F!"))  # expected: True
