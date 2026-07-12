"""Jewels and Stones — LeetCode 771."""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # TODO: put the jewel types in a set, then scan the stones
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numJewelsInStones("aA", "aAAbbbb"))  # expected: 3
    print(sol.numJewelsInStones("z", "ZZ"))  # expected: 0
