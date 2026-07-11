from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """Return every word that is a substring of another word in ``words``.

        A word is a substring of another only if it appears inside a *different*
        element of the list (a word is never its own answer). The intended
        scalable approach builds one Aho-Corasick automaton over all words and
        pushes each word through it, but any correct method is acceptable.

        Args:
            words: A list of distinct lowercase strings, 1 <= len <= 100,
                each of length 1..30.

        Returns:
            A list containing, in any order, each word of ``words`` that occurs
            as a contiguous substring of some other word.

        Example:
            >>> Solution().stringMatching(["mass", "as", "hero", "superhero"])
            ['as', 'hero']
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.stringMatching(["mass", "as", "hero", "superhero"]))
    # Expected (order may vary): ['as', 'hero']
    print(sol.stringMatching(["leetcode", "et", "code"]))
    # Expected (order may vary): ['et', 'code']
    print(sol.stringMatching(["blue", "green", "bu"]))
    # Expected: []
