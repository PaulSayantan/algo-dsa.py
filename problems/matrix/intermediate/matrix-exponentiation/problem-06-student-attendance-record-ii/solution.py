"""Student Attendance Record II (LeetCode 552), large-n variant, modulo 1e9+7.

Fill in the body using Matrix Exponentiation on the 6-state automaton so it
runs in O(log n). Do NOT use an O(n) loop — n can be as large as 10**18.
"""

MOD = 10**9 + 7


class Solution:
    def checkRecord(self, n: int) -> int:
        """Return the number of rewardable length-n attendance records, mod 1e9+7.

        A record over {'A','L','P'} is rewardable iff it has fewer than 2 'A's
        total and never has 3 or more consecutive 'L's.

        Args:
            n: Length of the attendance record, 1 <= n <= 10**18.

        Returns:
            Count of rewardable records of length n, modulo 10**9 + 7.

        Example:
            >>> Solution().checkRecord(2)
            8
        """
        # TODO: implement using matrix exponentiation.
        #   State = (A_count in {0,1}, trailing_L in {0,1,2}) -> 6 states.
        #   Build the 6x6 transition matrix for appending one of A/L/P,
        #   raise it to the n-th power, apply it to the start state
        #   (0 A's, 0 trailing L), and sum over all reachable end states.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkRecord(1))  # expected: 3
    print(sol.checkRecord(2))  # expected: 8
    print(sol.checkRecord(3))  # expected: 19
