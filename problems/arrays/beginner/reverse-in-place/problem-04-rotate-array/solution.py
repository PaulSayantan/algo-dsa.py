from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Rotate ``nums`` to the right by ``k`` steps, in place.

        Args:
            nums: The integer array to rotate. Modified in place.
            k: The (non-negative) number of steps to rotate right. May exceed
                ``len(nums)``.

        Returns:
            None. ``nums`` is mutated so its elements are rotated right by
            ``k`` positions.

        Example:
            >>> arr = [1, 2, 3, 4, 5, 6, 7]
            >>> Solution().rotate(arr, 3)
            >>> arr
            [5, 6, 7, 1, 2, 3, 4]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(arr, 3)
    print(arr)  # expected: [5, 6, 7, 1, 2, 3, 4]

    arr2 = [-1, -100, 3, 99]
    Solution().rotate(arr2, 2)
    print(arr2)  # expected: [3, 99, -1, -100]
