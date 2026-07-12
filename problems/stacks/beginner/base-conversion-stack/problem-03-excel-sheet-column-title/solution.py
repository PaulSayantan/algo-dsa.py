"""Convert a 1-indexed column number to its Excel column title (bijective base-26)."""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # TODO: subtract 1 each step, push 'A' + n%26 onto a stack, then n//=26; pop to read
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.convertToTitle(1))  # expected: 'A'
    print(sol.convertToTitle(26))  # expected: 'Z'
    print(sol.convertToTitle(28))  # expected: 'AB'
    print(sol.convertToTitle(701))  # expected: 'ZY'
