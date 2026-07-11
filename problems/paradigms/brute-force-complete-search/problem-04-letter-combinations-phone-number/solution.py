"""Letter Combinations of a Phone Number — Brute Force practice template.

Fill in the body of `letter_combinations`. Do NOT look at SOLUTION.md until you
have tried.
"""
from typing import List


class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        """Return every letter combination the phone number could spell.

        Args:
            digits: A string of digits, each in '2'..'9', length 0 to 4.

        Returns:
            A list of all possible letter strings (one letter chosen per digit).
            Returns an empty list when `digits` is empty. Order does not matter.

        Example:
            >>> sorted(Solution().letter_combinations("2"))
            ['a', 'b', 'c']
        """
        # Keypad mapping you will need:
        # phone = {
        #     "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        #     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        # }
        # TODO: implement using Brute Force / Complete Search
        # (build the Cartesian product of the per-digit letter sets).
        pass


if __name__ == "__main__":
    sol = Solution()
    # expected (any order): ad ae af bd be bf cd ce cf
    print(sol.letter_combinations("23"))
    print(sol.letter_combinations(""))   # expected: []
    print(sol.letter_combinations("2"))  # expected (any order): a b c
