"""Last Stone Weight — LeetCode 1046.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """Smash the two heaviest stones until at most one remains.

        On each turn take the two heaviest stones x <= y. If x == y both are
        destroyed; otherwise a stone of weight y - x remains. Return the weight
        of the final stone, or 0 if none remain.

        Args:
            stones: Positive integer weights of the stones.

        Returns:
            The weight of the last remaining stone, or 0 if all are destroyed.

        Example:
            >>> Solution().lastStoneWeight([2, 7, 4, 1, 8, 1])
            1
            >>> Solution().lastStoneWeight([3, 3])
            0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))  # expected: 1
    print(sol.lastStoneWeight([1]))                 # expected: 1
    print(sol.lastStoneWeight([3, 3]))              # expected: 0
