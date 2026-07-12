"""First Unique Character in a String — LeetCode 387."""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # TODO: count characters, then return the index of the first with count 1
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))  # expected: 0
    print(sol.firstUniqChar("loveleetcode"))  # expected: 2
    print(sol.firstUniqChar("aabb"))  # expected: -1
    print(sol.firstUniqChar("z"))  # expected: 0
