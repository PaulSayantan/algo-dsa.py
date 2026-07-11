from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """Return the start indices of every anagram of ``p`` found in ``s``.

        Args:
            s: The text string of lowercase English letters to search within.
            p: The pattern string whose anagrams (permutations) are sought.

        Returns:
            A list of 0-based start indices ``i`` such that the substring
            ``s[i : i + len(p)]`` is an anagram of ``p``. Order is unspecified.

        Example:
            >>> Solution().findAnagrams("cbaebabacd", "abc")
            [0, 6]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd", "abc"))  # expected: [0, 6]
    print(sol.findAnagrams("abab", "ab"))          # expected: [0, 1, 2]
    print(sol.findAnagrams("aa", "bb"))            # expected: []
