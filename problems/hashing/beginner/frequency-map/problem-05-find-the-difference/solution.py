"""Find the Difference — LeetCode 389."""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # TODO: t is s plus one extra letter (shuffled); return that letter
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))  # expected: 'e'
    print(sol.findTheDifference("", "y"))  # expected: 'y'
    print(sol.findTheDifference("a", "aa"))  # expected: 'a'
    print(sol.findTheDifference("ae", "aea"))  # expected: 'a'
