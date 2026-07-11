from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """Return the k-th smallest absolute distance among all pairs in ``nums``.

        The distance of a pair (i, j) with i < j is ``abs(nums[i] - nums[j])``.
        Distances are considered in sorted order, duplicates counted separately.

        Args:
            nums: The input integer array.
            k: 1-indexed rank of the distance to return
                (``1 <= k <= n*(n-1)//2``).

        Returns:
            The k-th smallest pairwise distance.

        Example:
            >>> Solution().smallestDistancePair([1, 3, 1], 1)
            0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestDistancePair([1, 3, 1], 1))  # expected: 0
    print(sol.smallestDistancePair([1, 1, 1], 2))  # expected: 0
    print(sol.smallestDistancePair([1, 6, 1], 3))  # expected: 5
