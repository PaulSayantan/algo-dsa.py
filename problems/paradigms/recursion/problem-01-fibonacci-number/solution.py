"""Fibonacci Number — LeetCode 509.

Empty solution template. Fill in the body yourself using Recursion.
"""


class Solution:
    def fib(self, n: int) -> int:
        """Return the n-th Fibonacci number F(n).

        The sequence is defined by F(0) = 0, F(1) = 1, and
        F(n) = F(n - 1) + F(n - 2) for n > 1. Solve it with Recursion:
        handle the two base cases directly, and otherwise return the sum
        of the recursive calls on the two smaller subproblems.

        Args:
            n: A non-negative integer index into the Fibonacci sequence
               (0 <= n <= 30).

        Returns:
            The n-th Fibonacci number.

        Example:
            >>> Solution().fib(2)
            1
            >>> Solution().fib(4)
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(2))   # expected: 1
    print(sol.fib(3))   # expected: 2
    print(sol.fib(4))   # expected: 3
    print(sol.fib(10))  # expected: 55
