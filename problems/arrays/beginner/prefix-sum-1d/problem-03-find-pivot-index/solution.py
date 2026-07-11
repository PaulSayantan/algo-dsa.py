from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """Return the leftmost pivot index, or -1 if none exists.

        A pivot index i satisfies sum(nums[0..i-1]) == sum(nums[i+1..n-1]).

        Args:
            nums: A list of integers.

        Returns:
            The leftmost index where the left-side sum equals the right-side
            sum, or -1 if no such index exists.

        Example:
            >>> Solution().pivotIndex([1, 7, 3, 6, 5, 6])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    # Sample run — expected outputs shown as comments, not asserted.
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))  # expected: 3
    print(Solution().pivotIndex([1, 2, 3]))            # expected: -1
    print(Solution().pivotIndex([2, 1, -1]))           # expected: 0
