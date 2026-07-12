"""Clumsy Factorial — LeetCode 1006."""


class Solution:
    def clumsy(self, n: int) -> int:
        # TODO: term stack; fold * and / into the last term, then sum
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.clumsy(4))  # expected: 7
    print(sol.clumsy(1))  # expected: 1
    print(sol.clumsy(3))  # expected: 6
    print(sol.clumsy(10))  # expected: 12
    print(sol.clumsy(11))  # expected: 10
