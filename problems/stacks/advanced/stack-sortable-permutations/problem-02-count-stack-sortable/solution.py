"""Count stack-sortable permutations of 1..n (Catalan number)."""


class Solution:
    def countStackSortable(self, n: int) -> int:
        # TODO: return the n-th Catalan number
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countStackSortable(0))  # expected: 1
    print(sol.countStackSortable(3))  # expected: 5
    print(sol.countStackSortable(4))  # expected: 14
    print(sol.countStackSortable(5))  # expected: 42
