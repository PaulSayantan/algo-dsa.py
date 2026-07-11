from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """Return the maximum score from taking ``k`` cards off the two ends.

        Each step you remove one card from either the front or the back of the
        row; after exactly ``k`` steps your score is the sum of cards taken.

        Args:
            cardPoints: Points on each card, left to right.
            k: The exact number of cards to take, with ``1 <= k <= len(cardPoints)``.

        Returns:
            The largest total score achievable over all valid front/back splits.

        Example:
            >>> Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3)
            12
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxScore([1, 2, 3, 4, 5, 6, 1], 3))        # expected: 12
    print(sol.maxScore([2, 2, 2], 2))                     # expected: 4
    print(sol.maxScore([9, 7, 7, 9, 7, 7, 9], 7))         # expected: 55
