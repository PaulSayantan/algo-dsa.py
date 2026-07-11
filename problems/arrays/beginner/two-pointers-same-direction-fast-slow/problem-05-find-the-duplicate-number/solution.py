from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Find the single repeated value in `nums` without modifying it.

        `nums` has length n + 1 with values in [1, n]; exactly one value is
        repeated (possibly many times). Must use O(1) extra space and must not
        modify `nums`.

        Args:
            nums: The integer array (length n + 1, values in [1, n]).

        Returns:
            The repeated integer.

        Example:
            >>> Solution().findDuplicate([1, 3, 4, 2, 2])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().findDuplicate([3, 1, 3, 4, 2]))
    # Expected: 3
