"""Make The String Great — LeetCode 1544."""


class Solution:
    def makeGood(self, s: str) -> str:
        # TODO: stack; pop when top is the same letter as s in the opposite case
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.makeGood("leEeetcode"))  # expected: 'leetcode'
    print(sol.makeGood("abBAcC"))  # expected: ''
    print(sol.makeGood("s"))  # expected: 's'
