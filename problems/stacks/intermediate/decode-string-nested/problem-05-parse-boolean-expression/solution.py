"""Parse Boolean Expression — LeetCode 1106."""


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # TODO: stack fold; on ')' pop operands to '(', apply the operator beneath
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.parseBoolExpr("!(f)"))  # expected: True
    print(sol.parseBoolExpr("|(f,t)"))  # expected: True
    print(sol.parseBoolExpr("&(t,f)"))  # expected: False
    print(sol.parseBoolExpr("|(&(t,f,t),!(t))"))  # expected: False
    print(sol.parseBoolExpr("!(&(f,t))"))  # expected: True
