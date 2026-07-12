"""Relative Path Between Directories — os.path.relpath for absolute Unix paths."""


class Solution:
    def relativePath(self, from_path: str, to_path: str) -> str:
        # TODO: canonicalize both into component stacks, strip the common
        # prefix, emit '..' per leftover source part, then the leftover dest
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.relativePath("/a/b/c", "/a/b/d/e"))  # expected: '../d/e'
    print(sol.relativePath("/a/b", "/a/b"))  # expected: '.'
    print(sol.relativePath("/a/x/./y/../z", "/a/b"))  # expected: '../../b'
    print(sol.relativePath("/a/b/c", "/"))  # expected: '../../..'
