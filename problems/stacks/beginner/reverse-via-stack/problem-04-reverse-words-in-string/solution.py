"""Reverse the order of words in a sentence using a stack."""


class Solution:
    def reverseWords(self, s: str) -> str:
        # TODO: split into words, push each onto a stack, then pop to rejoin
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("the sky is blue"))  # expected: 'blue is sky the'
    print(sol.reverseWords("hello world"))  # expected: 'world hello'
    print(sol.reverseWords("a"))  # expected: 'a'
