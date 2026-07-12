"""Isomorphic Strings — LeetCode 205. Is there a consistent 1-to-1 char mapping?"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # TODO: maintain two maps (s->t and t->s) to enforce a bijection
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))  # expected: True
    print(sol.isIsomorphic("foo", "bar"))  # expected: False
    print(sol.isIsomorphic("paper", "title"))  # expected: True
    print(sol.isIsomorphic("badc", "baba"))  # expected: False
    print(sol.isIsomorphic("ab", "aa"))  # expected: False
