"""Valid Anagram — LeetCode 242."""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # TODO: two strings are anagrams iff their letter-frequency maps match
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # expected: True
    print(sol.isAnagram("rat", "car"))  # expected: False
    print(sol.isAnagram("a", "ab"))  # expected: False
    print(sol.isAnagram("listen", "silent"))  # expected: True
