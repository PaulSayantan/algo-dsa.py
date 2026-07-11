from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Return the kth largest element of ``nums`` (by sorted order).

        Intended approach: quickselect using a Dutch National Flag 3-way
        partition, giving expected O(n) time and robust handling of duplicate
        values. Do not fully sort the array.

        Args:
            nums: The list of integers to search (may be reordered in place).
            k: 1-based rank from the largest end (1 = maximum).

        Returns:
            The value that would occupy position k from the largest in sorted
            order.

        Example:
            >>> Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))              # expected: 5
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))     # expected: 4
    print(s.findKthLargest([1], 1))                             # expected: 1
