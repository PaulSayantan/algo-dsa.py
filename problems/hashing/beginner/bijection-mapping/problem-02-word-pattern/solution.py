"""Word Pattern — LeetCode 290."""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # TODO: enforce a bijection between pattern letters and words
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))  # expected: True
    print(sol.wordPattern("abba", "dog cat cat fish"))  # expected: False
    print(sol.wordPattern("aaaa", "dog cat cat dog"))  # expected: False
    print(sol.wordPattern("abba", "dog dog dog dog"))  # expected: False
