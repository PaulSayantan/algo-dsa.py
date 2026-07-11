"""Knight Dialer (LeetCode 935), large-n variant, modulo 1e9+7.

Fill in the body using Matrix Exponentiation on the 10x10 knight-move
transition matrix so it runs in O(log n). Do NOT use an O(n) loop — n can be
as large as 5*10**9.
"""

MOD = 10**9 + 7


class Solution:
    def knightDialer(self, n: int) -> int:
        """Return the number of length-n knight-dialer numbers, modulo 1e9+7.

        The knight starts on any digit and makes exactly n-1 valid knight
        jumps on the phone keypad.

        Args:
            n: Length of the dialed number, 1 <= n <= 5*10**9.

        Returns:
            Count of valid length-n numbers, modulo 10**9 + 7.

        Example:
            >>> Solution().knightDialer(2)
            20
        """
        # TODO: implement using matrix exponentiation.
        #   Build the 10x10 transition matrix from the knight-move adjacency,
        #   raise it to the (n-1)-th power, apply it to the all-ones vector,
        #   and sum the entries.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.knightDialer(1))  # expected: 10
    print(sol.knightDialer(2))  # expected: 20
    print(sol.knightDialer(3))  # expected: 46
