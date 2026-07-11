"""LeetCode 71 - Simplify Path.

Fill in the body of `simplifyPath`. Do not modify the signature.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        """Convert an absolute Unix path to its simplified canonical form.

        Rules: '.' means current dir, '..' means parent dir, repeated slashes
        collapse, and other dot-sequences (like '...') are normal names.

        Args:
            path: An absolute Unix-style path beginning with '/'.

        Returns:
            The simplified canonical path (starts with '/', no trailing slash
            unless it is the root).

        Example:
            >>> Solution().simplifyPath("/a/./b/../../c/")
            '/c'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath("/home/"))              # expected: "/home"
    print(sol.simplifyPath("/home//foo/"))         # expected: "/home/foo"
    print(sol.simplifyPath("/a/./b/../../c/"))     # expected: "/c"
