"""Score of Parentheses — LeetCode 856."""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # TODO: stack of frame scores; '(' pushes 0, ')' folds max(2*inner, 1) up
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.scoreOfParentheses("()"))  # expected: 1
    print(sol.scoreOfParentheses("(())"))  # expected: 2
    print(sol.scoreOfParentheses("()()"))  # expected: 2
    print(sol.scoreOfParentheses("(()(()))"))  # expected: 6
