"""Pow(x, n) — LeetCode 50.

Empty solution template. Fill in the body yourself using Recursion.
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Compute x raised to the power n (x ** n) without built-in pow.

        Solve it with Recursion using fast exponentiation: x^n = (x^(n/2))^2.
        Compute the half power once, square it, and fold in one extra factor of
        x when n is odd. Handle negative exponents via the reciprocal, and use
        n == 0 as the base case (x^0 = 1).

        Args:
            x: The floating-point base (-100.0 < x < 100.0).
            n: The integer exponent, possibly negative.

        Returns:
            The value of x ** n as a float.

        Example:
            >>> Solution().myPow(2.0, 10)
            1024.0
            >>> Solution().myPow(2.0, -2)
            0.25
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.0, 10))   # expected: 1024.0
    print(sol.myPow(2.1, 3))    # expected: ~9.261
    print(sol.myPow(2.0, -2))   # expected: 0.25
    print(sol.myPow(3.0, 0))    # expected: 1.0
