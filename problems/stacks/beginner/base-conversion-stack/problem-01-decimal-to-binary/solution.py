"""Convert a non-negative integer to binary using a stack."""


class Solution:
    def toBinary(self, n: int) -> str:
        # TODO: repeated division by 2, remainders on a stack
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.toBinary(0))  # expected: '0'
    print(sol.toBinary(5))  # expected: '101'
    print(sol.toBinary(10))  # expected: '1010'
    print(sol.toBinary(255))  # expected: '11111111'
