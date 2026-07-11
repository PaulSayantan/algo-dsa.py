from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """Return the count of numbers in ``nums`` that have an even digit count.

        Args:
            nums: A list of positive integers.

        Returns:
            The number of elements whose decimal representation has an even
            number of digits.

        Example:
            >>> Solution().findNumbers([12, 345, 2, 6, 7896])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findNumbers([12, 345, 2, 6, 7896]))   # expected: 2
    print(sol.findNumbers([555, 901, 482, 1771]))   # expected: 1
