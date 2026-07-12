"""Sandboxed Path Resolution — resolve a user path inside a root jail."""


class Solution:
    def safeResolve(self, root: str, user_path: str) -> str:
        # TODO: seed the stack with root's parts, fold in user_path, then reject
        # (return '') if the result no longer starts with root's parts
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.safeResolve("/var/www", "images/logo.png"))  # expected: '/var/www/images/logo.png'
    print(sol.safeResolve("/var/www", "../../etc/passwd"))  # expected: ''
    print(sol.safeResolve("/var/www", "a/../b/./c"))  # expected: '/var/www/b/c'
    print(sol.safeResolve("/srv", "."))  # expected: '/srv'
