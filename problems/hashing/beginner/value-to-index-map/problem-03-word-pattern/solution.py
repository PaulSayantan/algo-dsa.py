"""Word Pattern — LeetCode 290. Does pattern bijectively match the words of s?"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # TODO: split s into words; map char<->word both ways
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))  # expected: True
    print(sol.wordPattern("abba", "dog cat cat fish"))  # expected: False
    print(sol.wordPattern("aaaa", "dog cat cat dog"))  # expected: False
    print(sol.wordPattern("abba", "dog dog dog dog"))  # expected: False
    print(sol.wordPattern("abc", "b c a"))  # expected: True
