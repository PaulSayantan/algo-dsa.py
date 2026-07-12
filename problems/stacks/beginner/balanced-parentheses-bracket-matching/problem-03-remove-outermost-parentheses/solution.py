"""Remove Outermost Parentheses — LeetCode 1021."""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # TODO: track depth; skip the '(' opening and ')' closing each primitive
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeOuterParentheses("(()())(())"))  # expected: '()()()'
    print(sol.removeOuterParentheses("(())"))  # expected: '()'
    print(sol.removeOuterParentheses("()()"))  # expected: ''
    print(sol.removeOuterParentheses("(()(()))"))  # expected: '()(())'
