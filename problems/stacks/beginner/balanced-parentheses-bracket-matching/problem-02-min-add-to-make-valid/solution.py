"""Minimum Add to Make Parentheses Valid — LeetCode 921."""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # TODO
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minAddToMakeValid("())"))  # expected: 1
    print(sol.minAddToMakeValid("((("))  # expected: 3
    print(sol.minAddToMakeValid("()"))  # expected: 0
    print(sol.minAddToMakeValid("()))(("))  # expected: 4
