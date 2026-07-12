"""Asteroid Collision with Mass Absorption — mass-conserving variant of LeetCode 735."""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # TODO: stack of survivors; the bigger asteroid absorbs the destroyed one's mass
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.asteroidCollision([5, 10, -5]))  # expected: [5, 15]
    print(sol.asteroidCollision([8, -8]))  # expected: []
    print(sol.asteroidCollision([10, 2, -5]))  # expected: [17]
    print(sol.asteroidCollision([-2, -1, 1, 2]))  # expected: [-2, -1, 1, 2]
    print(sol.asteroidCollision([4, -1, -2, -8]))  # expected: [-15]
    print(sol.asteroidCollision([3, -4, 5]))  # expected: [-7, 5]
