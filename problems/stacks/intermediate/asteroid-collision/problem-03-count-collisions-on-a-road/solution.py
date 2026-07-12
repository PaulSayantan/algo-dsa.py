"""Count Collisions on a Road — LeetCode 2211."""


class Solution:
    def countCollisions(self, directions: str) -> int:
        # TODO: stack of moving cars; an approaching L/S annihilates the R pile
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countCollisions("RLRSLL"))  # expected: 5
    print(sol.countCollisions("LLRR"))  # expected: 0
    print(sol.countCollisions("RLRR"))  # expected: 2
    print(sol.countCollisions("SSRSSRLLRSLLRSSLS"))  # expected: 9
