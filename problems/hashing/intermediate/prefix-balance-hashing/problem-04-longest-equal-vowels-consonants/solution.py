"""Longest substring with equal numbers of vowels and consonants."""


class Solution:
    def longestEqualVowelConsonant(self, s: str) -> int:
        # TODO: vowel -> +1, consonant -> -1; equal counts means equal running
        #       balance at the substring ends. Earliest-index map (seed {0: -1}).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestEqualVowelConsonant("abcde"))  # expected: 2
    print(sol.longestEqualVowelConsonant("aeiou"))  # expected: 0
    print(sol.longestEqualVowelConsonant("leetcode"))  # expected: 8
    print(sol.longestEqualVowelConsonant("a"))  # expected: 0
    print(sol.longestEqualVowelConsonant("baba"))  # expected: 4
