"""Fibonacci Number — LeetCode 509.

Empty solution template. Fill in the body yourself.
"""


class Solution:
    def fib(self, n: int) -> int:
        """Return the nth Fibonacci number, where F(0) = 0 and F(1) = 1.

        Args:
            n: A non-negative integer index into the Fibonacci sequence (0 <= n <= 30).

        Returns:
            The value F(n).

        Example:
            >>> Solution().fib(10)
            55
        """
        # TODO: implement using memoization (top-down) or tabulation (bottom-up).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(2))   # expected: 1
    print(sol.fib(4))   # expected: 3
    print(sol.fib(10))  # expected: 55
