from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Sort an array of 0s, 1s, and 2s in place in ascending order.

        Do not return anything; modify ``nums`` in place instead. Aim for a
        single pass with O(1) extra space (Dutch National Flag).

        Args:
            nums: A list where each element is 0, 1, or 2.

        Returns:
            None. ``nums`` is mutated in place.

        Example:
            >>> s = Solution()
            >>> arr = [2, 0, 2, 1, 1, 0]
            >>> s.sortColors(arr)
            >>> arr
            [0, 0, 1, 1, 2, 2]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()

    a = [2, 0, 2, 1, 1, 0]
    s.sortColors(a)
    print(a)  # expected: [0, 0, 1, 1, 2, 2]

    b = [2, 0, 1]
    s.sortColors(b)
    print(b)  # expected: [0, 1, 2]
