"""Remove All Adjacent Duplicates in String II — LeetCode 1209."""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # TODO: stack of [char, run-length]; pop when run reaches k
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates("abcd", 2))  # expected: 'abcd'
    print(sol.removeDuplicates("deeedbbcccbdaa", 3))  # expected: 'aa'
    print(sol.removeDuplicates("pbbcggttciiippooaais", 2))  # expected: 'ps'
