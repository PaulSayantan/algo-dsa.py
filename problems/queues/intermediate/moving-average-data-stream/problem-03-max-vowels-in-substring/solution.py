"""Maximum Number of Vowels in a Substring of Given Length — LeetCode 1456."""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # TODO: slide a size-k window tracking a running vowel count; keep the max
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxVowels("abciiidef", 3))  # expected: 3
    print(sol.maxVowels("aeiou", 2))  # expected: 2
    print(sol.maxVowels("leetcode", 3))  # expected: 2
    print(sol.maxVowels("rhythms", 4))  # expected: 0
