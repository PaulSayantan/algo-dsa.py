"""Simplify Path — LeetCode 71."""


class Solution:
    def simplifyPath(self, path: str) -> str:
        # TODO: stack of path components
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath("/home/"))  # expected: '/home'
    print(sol.simplifyPath("/../"))  # expected: '/'
    print(sol.simplifyPath("/home//foo/"))  # expected: '/home/foo'
    print(sol.simplifyPath("/a/./b/../../c/"))  # expected: '/c'
    print(sol.simplifyPath("/a/../../b/../c//.//"))  # expected: '/c'
