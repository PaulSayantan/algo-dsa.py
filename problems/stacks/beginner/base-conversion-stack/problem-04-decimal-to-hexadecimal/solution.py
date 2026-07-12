"""Convert a 32-bit integer to lowercase hexadecimal using a stack of remainders."""


class Solution:
    def toHex(self, num: int) -> str:
        # TODO: mask to 32 bits, push num%16 as a hex digit, num//=16; pop to build
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.toHex(0))  # expected: '0'
    print(sol.toHex(26))  # expected: '1a'
    print(sol.toHex(255))  # expected: 'ff'
    print(sol.toHex(-1))  # expected: 'ffffffff'
