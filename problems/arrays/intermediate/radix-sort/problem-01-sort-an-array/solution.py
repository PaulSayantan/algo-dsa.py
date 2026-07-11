from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Sort an integer array in ascending order using radix sort.

        The array may contain negative numbers, zeros, and duplicates, so a
        plain non-negative radix sort is not enough on its own; you must account
        for negative values (for example, by offsetting every element or by
        sorting magnitudes and reversing the negative portion).

        Args:
            nums: List of integers to sort. May include negatives and
                duplicates.

        Returns:
            A list containing the same elements as ``nums`` in non-decreasing
            order.

        Example:
            >>> Solution().sortArray([5, 2, 3, 1])
            [1, 2, 3, 5]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().sortArray([5, 2, 3, 1]))
    # Expected: [1, 2, 3, 5]
    print(Solution().sortArray([5, 1, 1, 2, 0, 0]))
    # Expected: [0, 0, 1, 1, 2, 5]
    print(Solution().sortArray([-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]))
    # Expected: [-7, -5, -4, -1, -1, 0, 0, 4, 7, 9]
