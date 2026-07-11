from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        """Return answer[i] = |leftSum[i] - rightSum[i]| for each index.

        leftSum[i] is the sum of elements strictly to the left of i, and
        rightSum[i] is the sum of elements strictly to the right of i. The
        element at index i is excluded from both.

        Args:
            nums: A list of positive integers.

        Returns:
            A list of the same length where each entry is the absolute
            difference between the left-side sum and the right-side sum at that
            index.

        Example:
            >>> Solution().leftRightDifference([10, 4, 8, 3])
            [15, 1, 11, 22]
        """
        # TODO: implement (build a suffix sum for the right side,
        #       maintain a running prefix sum for the left side)
        pass


if __name__ == "__main__":
    # Sample runs — expected outputs shown as comments, not asserted.
    sol = Solution()
    print(sol.leftRightDifference([10, 4, 8, 3]))  # expected: [15, 1, 11, 22]
    print(sol.leftRightDifference([1]))            # expected: [0]
    print(sol.leftRightDifference([1, 2, 3]))      # expected: [5, 2, 3]
