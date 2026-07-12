"""Basic Calculator II — LeetCode 227."""


class Solution:
    def calculate(self, s: str) -> int:
        # TODO: stack of terms; fold * and / into the last term
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate("3+2*2"))  # expected: 7
    print(sol.calculate(" 3/2 "))  # expected: 1
    print(sol.calculate(" 3+5 / 2 "))  # expected: 5
    print(sol.calculate("14-3/2"))  # expected: 13
