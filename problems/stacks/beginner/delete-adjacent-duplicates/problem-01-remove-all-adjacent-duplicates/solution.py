"""Remove All Adjacent Duplicates In String — LeetCode 1047."""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        # TODO: stack; pop when incoming char equals top
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates("abbaca"))  # expected: 'ca'
    print(sol.removeDuplicates("azxxzy"))  # expected: 'ay'
    print(sol.removeDuplicates("aaaa"))  # expected: ''
