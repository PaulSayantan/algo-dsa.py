"""LeetCode 191 - Number of 1 Bits (Hamming weight).

Fill in the body of `hammingWeight`. Try to use bitwise operations rather than
string conversion.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        """Return the number of set (1) bits in the binary form of `n`.

        Args:
            n: A non-negative integer (treated as a 32-bit unsigned value).

        Returns:
            The count of 1 bits in `n`.

        Example:
            >>> Solution().hammingWeight(11)
            3
        """
        # TODO: implement using the Brian Kernighan trick: n &= n - 1.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(11))   # expected: 3
    print(sol.hammingWeight(128))  # expected: 1
    print(sol.hammingWeight(0))    # expected: 0
