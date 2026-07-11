from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Move all zeros to the end in place, preserving non-zero order.

        Modifies `nums` in place and returns nothing. Must not allocate a copy
        of the array (O(1) extra space).

        Args:
            nums: The integer array to rearrange in place.

        Returns:
            None. The rearrangement is done directly on `nums`.

        Example:
            >>> a = [0, 1, 0, 3, 12]
            >>> Solution().moveZeroes(a)
            >>> a
            [1, 3, 12, 0, 0]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
    # Expected: [1, 3, 12, 0, 0]
