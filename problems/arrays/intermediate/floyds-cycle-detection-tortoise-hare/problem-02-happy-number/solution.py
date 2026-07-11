"""LeetCode 202 - Happy Number.

Determine whether repeatedly replacing a number with the sum of the squares of
its digits eventually reaches 1.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """Return True if ``n`` is a happy number.

        Args:
            n: A positive integer (1 <= n <= 2**31 - 1).

        Returns:
            ``True`` if the digit-square-sum process eventually reaches 1,
            ``False`` if it loops in a cycle that never includes 1.

        Example:
            >>> Solution().isHappy(19)
            True
            >>> Solution().isHappy(2)
            False
        """
        # TODO: implement
        # Hint: a helper that computes the sum of squared digits of a number is
        # the "next" function; run tortoise (one hop) and hare (two hops) on it.
        pass


if __name__ == "__main__":
    print(Solution().isHappy(19))  # Expected: True
    print(Solution().isHappy(2))   # Expected: False
    print(Solution().isHappy(1))   # Expected: True
