"""Convert an integer (possibly negative) to its base-7 string using a stack."""


class Solution:
    def convertToBase7(self, num: int) -> str:
        # TODO: track the sign, push abs(num)%7 and floor-divide by 7; pop to build
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.convertToBase7(0))  # expected: '0'
    print(sol.convertToBase7(100))  # expected: '202'
    print(sol.convertToBase7(-7))  # expected: '-10'
    print(sol.convertToBase7(8))  # expected: '11'
