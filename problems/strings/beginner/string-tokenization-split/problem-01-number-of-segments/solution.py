"""LeetCode 434 - Number of Segments in a String.

Fill in the body of `countSegments`. Do not modify the signature.
"""


class Solution:
    def countSegments(self, s: str) -> int:
        """Count the number of space-separated segments in ``s``.

        A segment is a maximal run of non-space characters. Leading, trailing,
        and repeated interior spaces do not create empty segments.

        Args:
            s: The input string. May be empty or all spaces.

        Returns:
            The number of non-space segments in ``s``.

        Example:
            >>> Solution().countSegments("Hello, my name is John")
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSegments("Hello, my name is John"))  # expected: 5
    print(sol.countSegments("Hello"))                    # expected: 1
    print(sol.countSegments("   "))                      # expected: 0
