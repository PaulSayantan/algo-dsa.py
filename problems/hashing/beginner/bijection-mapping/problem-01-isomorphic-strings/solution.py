"""Isomorphic Strings — LeetCode 205."""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # TODO: keep consistent forward AND backward character mappings
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))  # expected: True
    print(sol.isIsomorphic("foo", "bar"))  # expected: False
    print(sol.isIsomorphic("paper", "title"))  # expected: True
    print(sol.isIsomorphic("badc", "baba"))  # expected: False
