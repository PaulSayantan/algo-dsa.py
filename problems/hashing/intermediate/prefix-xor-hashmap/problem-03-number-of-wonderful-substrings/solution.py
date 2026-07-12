"""Number of Wonderful Substrings — LeetCode 1915."""


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # TODO: 10-bit parity bitmask prefix; a substring is wonderful iff its
        #       parity mask is 0 (all even) or a single bit (exactly one odd).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.wonderfulSubstrings("aba"))  # expected: 4
    print(sol.wonderfulSubstrings("aabb"))  # expected: 9
    print(sol.wonderfulSubstrings("ba"))  # expected: 2
    print(sol.wonderfulSubstrings("aaa"))  # expected: 6
    print(sol.wonderfulSubstrings("jj"))  # expected: 3
