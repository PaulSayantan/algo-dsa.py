"""Backspace String Compare — LeetCode 844."""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # TODO: build each string on a stack, popping the top on '#'
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.backspaceCompare("ab#c", "ad#c"))  # expected: True
    print(sol.backspaceCompare("ab##", "c#d#"))  # expected: True
    print(sol.backspaceCompare("a#c", "b"))  # expected: False
