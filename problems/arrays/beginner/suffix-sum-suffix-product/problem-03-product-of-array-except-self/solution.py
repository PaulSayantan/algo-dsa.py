from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Return answer[i] = product of every element except nums[i].

        Must run in O(n) time and must not use the division operator.

        Args:
            nums: A list of integers of length >= 2.

        Returns:
            A list of the same length where each entry is the product of all
            other elements.

        Example:
            >>> Solution().productExceptSelf([1, 2, 3, 4])
            [24, 12, 8, 6]
        """
        # TODO: implement (prefix product on the left * suffix product on the right)
        pass


if __name__ == "__main__":
    # Sample runs — expected outputs shown as comments, not asserted.
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))          # expected: [24, 12, 8, 6]
    print(sol.productExceptSelf([-1, 1, 0, -3, 3]))     # expected: [0, 0, 9, 0, 0]
