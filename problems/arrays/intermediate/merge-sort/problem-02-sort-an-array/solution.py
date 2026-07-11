from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Sort ``nums`` in ascending order using merge sort.

        Do not use any built-in sort. Aim for O(n log n) time.

        Args:
            nums: List of integers to sort.

        Returns:
            A list containing the same elements in non-decreasing order.

        Example:
            >>> Solution().sortArray([5, 2, 3, 1])
            [1, 2, 3, 5]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))        # expected: [1, 2, 3, 5]
    print(s.sortArray([5, 1, 1, 2, 0, 0]))  # expected: [0, 0, 1, 1, 2, 5]
    print(s.sortArray([-3, 0, -3, 2]))      # expected: [-3, -3, 0, 2]
