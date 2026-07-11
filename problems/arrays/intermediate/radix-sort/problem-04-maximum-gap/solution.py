from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """Return the largest gap between successive elements of the sorted array.

        Must run in linear time and linear space. The intended approach is to
        sort ``nums`` with radix sort (the values are bounded by 10^9, so a
        constant number of digit passes suffices), then scan the sorted array
        once, tracking the maximum difference between adjacent elements.

        Args:
            nums: List of non-negative integers (each in 0..10^9).

        Returns:
            The maximum difference between two successive elements of the sorted
            array, or 0 if ``nums`` has fewer than two elements.

        Example:
            >>> Solution().maximumGap([3, 6, 9, 1])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().maximumGap([3, 6, 9, 1]))
    # Expected: 3
    print(Solution().maximumGap([10]))
    # Expected: 0
    print(Solution().maximumGap([1, 1, 1, 1]))
    # Expected: 0
    print(Solution().maximumGap([100, 3, 2, 1]))
    # Expected: 97
