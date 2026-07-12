"""Steps until a linear-congruential state first repeats."""


class Solution:
    def stepsToRepeat(self, start: int, a: int, c: int, m: int) -> int:
        # TODO: iterate x = (a*x + c) % m from start; count steps to the first repeat
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.stepsToRepeat(0, 1, 3, 5))  # expected: 5
    print(sol.stepsToRepeat(0, 2, 3, 7))  # expected: 3
    print(sol.stepsToRepeat(1, 0, 0, 10))  # expected: 2
