from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        """Wrap every substring of ``s`` that appears in ``words`` with <b></b>.

        Overlapping or consecutive bolded regions are merged so that each
        maximal covered run of characters is surrounded by exactly one pair of
        tags. The intended approach builds an Aho-Corasick automaton over
        ``words``, scans ``s`` to mark every covered position, then merges the
        covered runs.

        Args:
            s: The string to annotate, length 1..1000 (or larger in the classic
                variant), letters and digits.
            words: The dictionary of substrings to bold; may be empty.

        Returns:
            ``s`` with <b> and </b> tags inserted around each maximal run of
            positions covered by some word.

        Example:
            >>> Solution().addBoldTag("abcxyz123", ["abc", "123"])
            '<b>abc</b>xyz<b>123</b>'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBoldTag("abcxyz123", ["abc", "123"]))
    # Expected: "<b>abc</b>xyz<b>123</b>"
    print(sol.addBoldTag("aaabbee", ["aaa", "aab", "bc", "aaabbee"]))
    # Expected: "<b>aaabbee</b>"
    print(sol.addBoldTag("leetcode", []))
    # Expected: "leetcode"
