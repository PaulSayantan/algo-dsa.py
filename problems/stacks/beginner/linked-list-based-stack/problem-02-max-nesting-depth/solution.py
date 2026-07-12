"""Maximum Nesting Depth of Parentheses — LeetCode 1614."""


class Solution:
    def maxDepth(self, s: str) -> int:
        # TODO: track running depth as a stack height
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))  # expected: 3
    print(sol.maxDepth("(1)+((2))+(((3)))"))  # expected: 3
    print(sol.maxDepth("8*3"))  # expected: 0
