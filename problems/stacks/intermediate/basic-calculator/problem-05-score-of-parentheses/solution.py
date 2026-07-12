"""Score of Parentheses — LeetCode 856."""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # TODO: push a 0 frame on '('; on ')' pop v and add max(2*v, 1) to the frame below
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.scoreOfParentheses("()"))  # expected: 1
    print(sol.scoreOfParentheses("(())"))  # expected: 2
    print(sol.scoreOfParentheses("()()"))  # expected: 2
    print(sol.scoreOfParentheses("(()(()))"))  # expected: 6
    print(sol.scoreOfParentheses("((()))"))  # expected: 4
