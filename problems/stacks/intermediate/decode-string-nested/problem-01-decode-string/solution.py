"""Decode String — LeetCode 394."""


class Solution:
    def decodeString(self, s: str) -> str:
        # TODO: stacks for counts and partial strings
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]"))  # expected: 'aaabcbc'
    print(sol.decodeString("3[a2[c]]"))  # expected: 'accaccacc'
    print(sol.decodeString("2[abc]3[cd]ef"))  # expected: 'abcabccdcdcdef'
    print(sol.decodeString("abc3[cd]xyz"))  # expected: 'abccdcdcdxyz'
