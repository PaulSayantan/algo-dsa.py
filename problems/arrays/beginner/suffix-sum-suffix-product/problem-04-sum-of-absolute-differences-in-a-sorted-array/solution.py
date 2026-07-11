from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """Return result[i] = sum over j of |nums[i] - nums[j]|.

        The input is sorted in non-decreasing order, which lets the sum be split
        into a left (smaller-or-equal) part and a right (greater-or-equal) part.

        Args:
            nums: A list of integers sorted in non-decreasing order.

        Returns:
            A list of the same length where each entry is the sum of absolute
            differences between that element and all elements of the array.

        Example:
            >>> Solution().getSumAbsoluteDifferences([2, 3, 5])
            [4, 3, 5]
        """
        # TODO: implement (use a prefix sum for the left side and a
        #       suffix sum for the right side)
        pass


if __name__ == "__main__":
    # Sample runs — expected outputs shown as comments, not asserted.
    sol = Solution()
    print(sol.getSumAbsoluteDifferences([2, 3, 5]))          # expected: [4, 3, 5]
    print(sol.getSumAbsoluteDifferences([1, 4, 6, 8, 10]))   # expected: [24, 15, 13, 15, 21]
