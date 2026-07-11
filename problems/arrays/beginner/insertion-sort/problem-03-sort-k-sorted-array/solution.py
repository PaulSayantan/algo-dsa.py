from typing import List


class Solution:
    def sortKSortedArray(self, nums: List[int], k: int) -> List[int]:
        """Sort a nearly-sorted (k-sorted) array using adaptive Insertion Sort.

        Every element is guaranteed to be at most ``k`` positions away from its
        final sorted position, so insertion sort shifts each element at most k
        places, giving O(n * k) time overall.

        Args:
            nums: The nearly-sorted array. 1 <= len(nums) <= 1e5.
            k: The maximum distance any element is from its sorted position.
                0 <= k < len(nums).

        Returns:
            ``nums`` sorted in ascending order (sorting in place is allowed).

        Example:
            >>> Solution().sortKSortedArray([3, 1, 2, 5, 4, 7, 6], 2)
            [1, 2, 3, 4, 5, 6, 7]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortKSortedArray([3, 1, 2, 5, 4, 7, 6], 2))   # expected: [1, 2, 3, 4, 5, 6, 7]
    print(sol.sortKSortedArray([2, 1, 3, 4], 1))            # expected: [1, 2, 3, 4]
    print(sol.sortKSortedArray([6, 5, 3, 2, 8, 10, 9], 3))  # expected: [2, 3, 5, 6, 8, 9, 10]
