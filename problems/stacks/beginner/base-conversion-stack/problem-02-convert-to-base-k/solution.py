"""Convert a non-negative integer to base k (2..16) using a stack."""


class Solution:
    def toBaseK(self, n: int, k: int) -> str:
        # TODO
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.toBaseK(255, 16))  # expected: 'ff'
    print(sol.toBaseK(8, 2))  # expected: '1000'
    print(sol.toBaseK(100, 8))  # expected: '144'
    print(sol.toBaseK(0, 5))  # expected: '0'
