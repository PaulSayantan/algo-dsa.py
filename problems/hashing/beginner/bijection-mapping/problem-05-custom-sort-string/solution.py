"""Custom Sort String — LeetCode 791."""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # TODO: map each letter to a rank from `order`, then stable-sort s by that rank
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.customSortString("cba", "abcd"))  # expected: 'cbad'
    print(sol.customSortString("bcafg", "abcd"))  # expected: 'bcad'
