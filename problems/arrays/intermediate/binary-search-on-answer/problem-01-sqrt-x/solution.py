"""Sqrt(x) — LeetCode 69.

Return floor(sqrt(x)) without using any built-in exponent/sqrt function.
Solve it with Binary Search on Answer over the range [0, x].
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """Return the largest integer k such that k * k <= x.

        Args:
            x: A non-negative integer (0 <= x <= 2^31 - 1).

        Returns:
            The integer square root of x (the square root rounded down).

        Example:
            >>> Solution().mySqrt(8)
            2
        """
        # TODO: implement using Binary Search on Answer over [0, x].
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))   # expected: 2
    print(sol.mySqrt(8))   # expected: 2
    print(sol.mySqrt(0))   # expected: 0
    print(sol.mySqrt(1))   # expected: 1
