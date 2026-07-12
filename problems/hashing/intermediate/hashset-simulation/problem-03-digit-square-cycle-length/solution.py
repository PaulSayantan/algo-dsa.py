"""Count distinct states before the sum-of-squared-digits sequence repeats."""


class Solution:
    def digitSquareCycle(self, start: int) -> int:
        # TODO: iterate until a value repeats; return the number of distinct values seen
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.digitSquareCycle(1))  # expected: 1
    print(sol.digitSquareCycle(7))  # expected: 6
    print(sol.digitSquareCycle(4))  # expected: 8
