"""Remove All Adjacent Duplicates In String — LeetCode 1047."""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        # TODO: push each char; if it equals the top of the stack, pop instead
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates("abbaca"))  # expected: 'ca'
    print(sol.removeDuplicates("azxxzy"))  # expected: 'ay'
    print(sol.removeDuplicates("aaaaaa"))  # expected: ''
    print(sol.removeDuplicates("abcd"))  # expected: 'abcd'
