"""4Sum II — LeetCode 454.

Count index tuples (i, j, k, l) with
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0.

Fill in `fourSumCount` using the Meet in the Middle idea: split the four
arrays into two independent pairs, enumerate the pair-sums of the first pair
into a hash map, then match against the pair-sums of the second pair.
"""

from typing import List


class Solution:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int],
    ) -> int:
        """Return the number of tuples (i, j, k, l) summing to zero.

        Args:
            nums1: First integer array of length n.
            nums2: Second integer array of length n.
            nums3: Third integer array of length n.
            nums4: Fourth integer array of length n.

        Returns:
            The count of index tuples (i, j, k, l) with
            nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0.

        Example:
            >>> Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # Expected: 2
    print(sol.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
    # Expected: 1
    print(sol.fourSumCount([0], [0], [0], [0]))
    # Expected: 6
    print(sol.fourSumCount([1, -1], [1, -1], [1, -1], [1, -1]))
