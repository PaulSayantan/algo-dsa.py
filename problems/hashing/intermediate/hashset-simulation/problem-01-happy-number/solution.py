"""Happy Number — LeetCode 202."""


class Solution:
    def isHappy(self, n: int) -> bool:
        # TODO: iterate sum-of-squared-digits; a repeat (in a seen set) ⇒ not happy
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))  # expected: True
    print(sol.isHappy(2))  # expected: False
    print(sol.isHappy(1))  # expected: True
    print(sol.isHappy(7))  # expected: True
