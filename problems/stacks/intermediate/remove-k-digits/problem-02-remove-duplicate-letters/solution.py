"""Remove Duplicate Letters — LeetCode 316."""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # TODO: greedy monotonic stack with last-occurrence lookahead
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicateLetters("bcabc"))  # expected: 'abc'
    print(sol.removeDuplicateLetters("cbacdcbc"))  # expected: 'acdb'
    print(sol.removeDuplicateLetters("abacb"))  # expected: 'abc'
