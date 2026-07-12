"""Removing Stars From a String — LeetCode 2390."""


class Solution:
    def removeStars(self, s: str) -> str:
        # TODO: push letters, a '*' pops the top (left-moving annihilation)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeStars("leet**cod*e"))  # expected: 'lecoe'
    print(sol.removeStars("erase*****"))  # expected: ''
    print(sol.removeStars("abc"))  # expected: 'abc'
    print(sol.removeStars("a*b*c*"))  # expected: ''
