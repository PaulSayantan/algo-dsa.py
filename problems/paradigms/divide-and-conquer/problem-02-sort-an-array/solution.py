"""Sort an Array — LeetCode 912.

Empty solution template. Implement merge sort (Divide and Conquer) yourself;
built-in sort is not allowed.
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Return nums sorted in ascending order using merge sort.

        Do not call any built-in sort. Split the array into halves, sort each
        recursively, then merge the two sorted halves in linear time.

        Args:
            nums: List of integers to sort.

        Returns:
            A list containing the same elements as nums in ascending order.

        Example:
            >>> Solution().sortArray([5, 2, 3, 1])
            [1, 2, 3, 5]
            >>> Solution().sortArray([5, 1, 1, 2, 0, 0])
            [0, 0, 1, 1, 2, 5]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortArray([5, 2, 3, 1]))          # expected: [1, 2, 3, 5]
    print(sol.sortArray([5, 1, 1, 2, 0, 0]))    # expected: [0, 0, 1, 1, 2, 5]
    print(sol.sortArray([3, -1, -1, 4]))        # expected: [-1, -1, 3, 4]
