"""LeetCode 324 - Wiggle Sort II.

Reorder in place to nums[0] < nums[1] > nums[2] < nums[3] ...
using Quickselect (median) plus a 3-way partition.
"""
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """Reorder nums in place into the strict wiggle pattern.

        Do not return anything; modify nums in place.

        Args:
            nums: List of integers with a guaranteed valid wiggle arrangement.

        Returns:
            None. nums is mutated so that nums[0] < nums[1] > nums[2] < ...

        Example:
            >>> a = [1, 5, 1, 1, 6, 4]
            >>> Solution().wiggleSort(a)
            >>> a[0] < a[1] > a[2] < a[3] > a[4] < a[5]
            True
        """
        # TODO: implement
        # Hint: 1) Quickselect the median;
        #       2) 3-way partition around the median using an index-mapping so
        #          that larger values fill odd slots and smaller values fill
        #          even slots (interleaving keeps equal medians apart).
        pass


if __name__ == "__main__":
    sol = Solution()

    a = [1, 5, 1, 1, 6, 4]
    sol.wiggleSort(a)
    # expected: a valid wiggle, e.g. [1, 6, 1, 5, 1, 4]

    b = [1, 3, 2, 2, 3, 1]
    sol.wiggleSort(b)
    # expected: a valid wiggle, e.g. [2, 3, 1, 3, 1, 2]

    c = [1, 2]
    sol.wiggleSort(c)
    # expected: [1, 2]

    def is_wiggle(x):
        return all((x[i] < x[i + 1]) if i % 2 == 0 else (x[i] > x[i + 1])
                   for i in range(len(x) - 1))

    print(is_wiggle(a), is_wiggle(b), is_wiggle(c))  # expected: True True True
