from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """Return the least ship capacity that ships all packages within ``days`` days.

        Each day loads a contiguous prefix of the remaining packages (in order)
        whose total weight does not exceed the capacity.

        Args:
            weights: Package weights in the order they sit on the belt.
            days: The maximum number of days allowed to ship everything.

        Returns:
            The minimum integer capacity that suffices.

        Example:
            >>> Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
            15
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # expected: 15
    print(sol.shipWithinDays([3, 2, 2, 4, 1, 4], 3))               # expected: 6
    print(sol.shipWithinDays([1, 2, 3, 1, 1], 4))                  # expected: 3
