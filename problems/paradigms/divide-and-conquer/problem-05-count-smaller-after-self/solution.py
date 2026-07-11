"""Count of Smaller Numbers After Self — LeetCode 315.

Empty solution template. Solve it with a merge-sort-based Divide and Conquer
that counts inversions during the merge.
"""
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """Return counts[i] = number of j > i with nums[j] < nums[i].

        Use a merge sort over (value, original index) pairs; during the merge,
        credit each left-half element with the number of right-half elements
        that are strictly smaller and thus sit to its right.

        Args:
            nums: List of integers.

        Returns:
            A list where entry i counts strictly-smaller elements to the right
            of nums[i].

        Example:
            >>> Solution().countSmaller([5, 2, 6, 1])
            [2, 1, 1, 0]
            >>> Solution().countSmaller([-1, -1])
            [0, 0]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSmaller([5, 2, 6, 1]))    # expected: [2, 1, 1, 0]
    print(sol.countSmaller([-1, -1]))        # expected: [0, 0]
    print(sol.countSmaller([3, 1, 2, 4]))    # expected: [2, 0, 0, 0]
