"""Backspace String Compare: build each string on a stack, '#' undoes a keypress."""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # TODO: build each string on a stack ('#' pops the last char), then compare
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.backspaceCompare("ab#c", "ad#c"))  # expected: True
    print(sol.backspaceCompare("a##c", "#a#c"))  # expected: True
    print(sol.backspaceCompare("a#c", "b"))      # expected: False
    print(sol.backspaceCompare("bxj##tw", "bxo#j##tw"))  # expected: True
