from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """Reorder ``nums`` in place into a strict wiggle pattern.

        The result must satisfy
        ``nums[0] < nums[1] > nums[2] < nums[3] ...``. Do not return anything;
        modify ``nums`` in place. A valid answer is guaranteed to exist.

        Intended approach: find the median with quickselect, then use a Dutch
        National Flag 3-way partition around the median combined with an
        index-mapping placement so equal values (especially copies of the
        median) never end up adjacent.

        Args:
            nums: The list of integers to reorder (mutated in place).

        Returns:
            None. ``nums`` is mutated in place.

        Example:
            >>> s = Solution()
            >>> arr = [1, 5, 1, 1, 6, 4]
            >>> s.wiggleSort(arr)
            >>> arr[0] < arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()

    a = [1, 5, 1, 1, 6, 4]
    s.wiggleSort(a)
    print(a)  # expected: a valid wiggle, e.g. [1, 6, 1, 5, 1, 4]

    b = [1, 3, 2, 2, 3, 1]
    s.wiggleSort(b)
    print(b)  # expected: a valid wiggle, e.g. [2, 3, 1, 3, 1, 2]
