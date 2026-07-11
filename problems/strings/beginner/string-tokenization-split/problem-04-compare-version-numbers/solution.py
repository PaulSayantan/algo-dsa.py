"""LeetCode 165 - Compare Version Numbers.

Fill in the body of `compareVersion`. Do not modify the signature.
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """Compare two dot-separated version strings.

        Revisions are compared left to right by integer value (leading zeros
        ignored). Missing trailing revisions count as 0.

        Args:
            version1: The first version string, e.g. "1.01".
            version2: The second version string, e.g. "1.001".

        Returns:
            -1 if version1 < version2, 1 if version1 > version2, else 0.

        Example:
            >>> Solution().compareVersion("1.2", "1.10")
            -1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.compareVersion("1.2", "1.10"))       # expected: -1
    print(sol.compareVersion("1.01", "1.001"))     # expected: 0
    print(sol.compareVersion("1.0", "1.0.0.0"))    # expected: 0
