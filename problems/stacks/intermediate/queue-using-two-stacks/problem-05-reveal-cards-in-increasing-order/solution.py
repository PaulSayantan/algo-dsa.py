"""Reveal Cards in Increasing Order — LeetCode 950 (two-stack FIFO of indices)."""
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # TODO: FIFO queue of positions; place sorted card at popped front,
        # then rotate the next front position to the back
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))  # expected: [2, 13, 3, 11, 5, 17, 7]
    print(sol.deckRevealedIncreasing([1, 1000]))  # expected: [1, 1000]
    print(sol.deckRevealedIncreasing([1, 2, 3, 4, 5, 6]))  # expected: [1, 4, 2, 6, 3, 5]
