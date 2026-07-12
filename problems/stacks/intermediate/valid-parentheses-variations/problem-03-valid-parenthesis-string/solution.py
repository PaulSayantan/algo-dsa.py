"""Valid Parenthesis String — LeetCode 678."""


class Solution:
    def checkValidString(self, s: str) -> bool:
        # TODO: track the [low, high] range of possible unmatched '(' counts
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkValidString("()"))  # expected: True
    print(sol.checkValidString("(*)"))  # expected: True
    print(sol.checkValidString("(*))"))  # expected: True
    print(sol.checkValidString(")("))  # expected: False
    print(sol.checkValidString("(((*)"))  # expected: False
