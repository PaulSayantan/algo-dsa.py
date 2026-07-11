from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """Return the minimum positive startValue keeping every step sum >= 1.

        Args:
            nums: A list of integers to be added, left to right, on top of
                startValue.

        Returns:
            The smallest positive integer startValue such that the running
            total (startValue + prefix of nums) is never below 1.

        Example:
            >>> Solution().minStartValue([-3, 2, -3, 4, 2])
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minStartValue([-3, 2, -3, 4, 2]))  # expected: 5
    print(sol.minStartValue([1, 2]))             # expected: 1
    print(sol.minStartValue([1, -2, -3]))        # expected: 5
