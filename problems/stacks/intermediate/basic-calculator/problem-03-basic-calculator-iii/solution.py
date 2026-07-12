"""Basic Calculator III — LeetCode 772."""


class Solution:
    def calculate(self, s: str) -> int:
        # TODO: term stack with * / folding; recurse (or push context) on '('
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate("1+1"))  # expected: 2
    print(sol.calculate("6-4/2"))  # expected: 4
    print(sol.calculate("2*(5+5*2)/3+(6/2+8)"))  # expected: 21
    print(sol.calculate("(2+6*3+5-(3*14/7+2)*5)+3"))  # expected: -12
    print(sol.calculate(" 2-1 + 2 "))  # expected: 3
