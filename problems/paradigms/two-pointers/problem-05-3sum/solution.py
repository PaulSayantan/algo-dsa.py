from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Return all unique triplets that sum to zero.

        Each returned triplet contains three elements drawn from distinct
        indices whose values add up to 0. No duplicate triplet (as a multiset of
        values) appears in the result.

        Args:
            nums: A list of integers.

        Returns:
            A list of triplets (each a list of three ints) summing to zero, with
            no duplicate triplets. Order of triplets is unspecified.

        Example:
            >>> Solution().threeSum([-1, 0, 1, 2, -1, -4])
            [[-1, -1, 2], [-1, 0, 1]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # expected: [[-1, -1, 2], [-1, 0, 1]]
    print(sol.threeSum([0, 1, 1]))              # expected: []
    print(sol.threeSum([0, 0, 0]))              # expected: [[0, 0, 0]]
