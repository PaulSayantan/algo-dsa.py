"""Minimum Remove to Make Valid Parentheses — LeetCode 1249."""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # TODO: index stack; delete unmatched parentheses
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))  # expected: 'lee(t(c)o)de'
    print(sol.minRemoveToMakeValid("a)b(c)d"))  # expected: 'ab(c)d'
    print(sol.minRemoveToMakeValid("))(("))  # expected: ''
