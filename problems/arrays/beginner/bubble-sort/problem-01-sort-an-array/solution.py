from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Sort an integer array in ascending order using Bubble Sort.

        Args:
            nums: A list of integers, possibly containing duplicates and
                negatives. 1 <= len(nums) <= 1000.

        Returns:
            The same values sorted in non-decreasing (ascending) order. You may
            sort in place and return ``nums`` or return a new list.

        Example:
            >>> Solution().sortArray([5, 2, 3, 1])
            [1, 2, 3, 5]
        """
        # implement bubble sort
        for _ in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortArray([5, 2, 3, 1]))            # expected: [1, 2, 3, 5]
    print(sol.sortArray([5, 1, 1, 2, 0, 0]))       # expected: [0, 0, 1, 1, 2, 5]
    print(sol.sortArray([-3, 0, -1, 2, -3]))       # expected: [-3, -3, -1, 0, 2]
