"""Climbing Stairs — LeetCode 70.

Empty solution template. Fill in the body yourself.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """Return the number of distinct ways to climb an n-step staircase.

        You may ascend either 1 or 2 steps at a time.

        Args:
            n: The total number of steps to the top (1 <= n <= 45).

        Returns:
            The count of distinct ordered sequences of 1- and 2-step moves summing to n.

        Example:
            >>> Solution().climbStairs(3)
            3
        """
        # TODO: implement using memoization (top-down) or tabulation (bottom-up).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))  # expected: 2
    print(sol.climbStairs(3))  # expected: 3
    print(sol.climbStairs(5))  # expected: 8
