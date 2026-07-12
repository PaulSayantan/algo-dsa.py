"""Remove K Digits — LeetCode 402."""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # TODO: monotonic increasing stack of digits
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeKdigits("1432219", 3))  # expected: '1219'
    print(sol.removeKdigits("10200", 1))  # expected: '200'
    print(sol.removeKdigits("10", 2))  # expected: '0'
    print(sol.removeKdigits("112", 1))  # expected: '11'
