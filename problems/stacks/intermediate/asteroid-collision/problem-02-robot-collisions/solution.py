"""Robot Collisions — LeetCode 2751."""
from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        # TODO: sort by position, then run an asteroid-collision stack of right-movers
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.survivedRobotsHealths([3, 5, 2, 6], [10, 10, 15, 12], "RLRL"))  # expected: [14]
    print(sol.survivedRobotsHealths([1, 2, 3], [5, 6, 7], "RRR"))  # expected: [5, 6, 7]
    print(sol.survivedRobotsHealths([1, 2], [5, 3], "RL"))  # expected: [4]
    print(sol.survivedRobotsHealths([1, 2], [5, 3], "LR"))  # expected: [5, 3]
