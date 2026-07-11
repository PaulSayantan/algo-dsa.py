from typing import List


class Solution:
    def find_max(self, nums: List[int]) -> int:
        """Return the largest value in a non-empty array.

        Args:
            nums: A non-empty list of integers (unsorted, may be negative).

        Returns:
            The maximum integer in ``nums``.

        Example:
            >>> Solution().find_max([3, 41, 52, 26])
            52
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.find_max([3, 41, 52, 26, 38, 57, 9, 49]))  # expected: 57
    print(sol.find_max([-7, -3, -19, -2, -11]))          # expected: -2
    print(sol.find_max([42]))                            # expected: 42
