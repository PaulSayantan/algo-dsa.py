"""Check if the Sentence Is Pangram — LeetCode 1832."""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # TODO: a pangram uses all 26 lowercase letters at least once
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))  # expected: True
    print(sol.checkIfPangram("leetcode"))  # expected: False
    print(sol.checkIfPangram("abcdefghijklmnopqrstuvwxyz"))  # expected: True
