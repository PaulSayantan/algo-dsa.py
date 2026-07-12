"""Maximum Number After Removing K Digits — maximize variant of LeetCode 402."""


class Solution:
    def removeKdigitsMax(self, num: str, k: int) -> str:
        # TODO: monotonic decreasing stack; pop a smaller top when a larger digit arrives
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeKdigitsMax("1432219", 3))  # expected: '4329'
    print(sol.removeKdigitsMax("1234", 2))  # expected: '34'
    print(sol.removeKdigitsMax("10", 1))  # expected: '1'
