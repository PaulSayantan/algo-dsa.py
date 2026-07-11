"""Fruit Into Baskets — empty solution template.

Fill in the body of `totalFruit`. Do not hard-code answers.
"""

from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """Return the max fruits picked with baskets holding at most 2 types.

        Args:
            fruits: A list where fruits[i] is the type of fruit at tree i.

        Returns:
            The length of the longest contiguous subarray of `fruits` that
            contains at most 2 distinct values.

        Example:
            >>> Solution().totalFruit([1, 2, 3, 2, 2])
            4
        """
        # TODO: implement using a variable-size sliding window
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.totalFruit([1, 2, 1]))        # expected: 3
    print(sol.totalFruit([0, 1, 2, 2]))     # expected: 3
    print(sol.totalFruit([1, 2, 3, 2, 2]))  # expected: 4
