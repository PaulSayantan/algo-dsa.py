class Solution:
    def mySqrt(self, x: int) -> int:
        """Return the integer square root of ``x`` (floor of the real sqrt).

        Equivalent to the largest non-negative integer ``k`` such that
        ``k * k <= x``. Built-in power/sqrt functions may not be used.

        Args:
            x: A non-negative integer, ``0 <= x <= 2**31 - 1``.

        Returns:
            The largest integer ``k`` with ``k * k <= x``.

        Example:
            >>> Solution().mySqrt(8)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))  # expected: 2
    print(sol.mySqrt(8))  # expected: 2
    print(sol.mySqrt(0))  # expected: 0
    print(sol.mySqrt(1))  # expected: 1
