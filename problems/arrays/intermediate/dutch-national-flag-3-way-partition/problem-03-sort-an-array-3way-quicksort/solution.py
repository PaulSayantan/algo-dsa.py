from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Sort ``nums`` in ascending order without a built-in sort.

        Intended approach: quicksort with a Dutch National Flag 3-way
        partition, so runs of equal keys are grouped in one pass and excluded
        from further recursion.

        Args:
            nums: The list of integers to sort (may be mutated in place).

        Returns:
            The list sorted in ascending order.

        Example:
            >>> Solution().sortArray([5, 1, 1, 2, 0, 0])
            [0, 0, 1, 1, 2, 5]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))        # expected: [1, 2, 3, 5]
    print(s.sortArray([5, 1, 1, 2, 0, 0]))  # expected: [0, 0, 1, 1, 2, 5]
    print(s.sortArray([3, 3, 3]))           # expected: [3, 3, 3]
