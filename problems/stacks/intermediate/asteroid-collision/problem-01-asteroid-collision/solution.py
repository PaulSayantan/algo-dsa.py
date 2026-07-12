"""Asteroid Collision — LeetCode 735."""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # TODO: stack simulation
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.asteroidCollision([5, 10, -5]))  # expected: [5, 10]
    print(sol.asteroidCollision([8, -8]))  # expected: []
    print(sol.asteroidCollision([10, 2, -5]))  # expected: [10]
    print(sol.asteroidCollision([-2, -1, 1, 2]))  # expected: [-2, -1, 1, 2]
