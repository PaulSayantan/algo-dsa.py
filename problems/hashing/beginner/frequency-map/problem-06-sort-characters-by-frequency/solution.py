"""Sort Characters By Frequency — LeetCode 451."""


class Solution:
    def frequencySort(self, s: str) -> str:
        # TODO: order characters by decreasing frequency, each repeated its count
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.frequencySort("aaabbc"))  # expected: 'aaabbc'
    print(sol.frequencySort("cccbba"))  # expected: 'cccbba'
    print(sol.frequencySort("eeeeddda"))  # expected: 'eeeeddda'
    print(sol.frequencySort("zzzy"))  # expected: 'zzzy'
