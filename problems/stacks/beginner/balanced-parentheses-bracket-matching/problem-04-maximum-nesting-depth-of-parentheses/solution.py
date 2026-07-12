"""Maximum Nesting Depth of the Parentheses — LeetCode 1614."""


class Solution:
    def maxDepth(self, s: str) -> int:
        # TODO: track current open-bracket count and its running maximum
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))  # expected: 3
    print(sol.maxDepth("(1)+((2))+(((3)))"))  # expected: 3
    print(sol.maxDepth("1+2"))  # expected: 0
    print(sol.maxDepth("()(())((()()))"))  # expected: 3
