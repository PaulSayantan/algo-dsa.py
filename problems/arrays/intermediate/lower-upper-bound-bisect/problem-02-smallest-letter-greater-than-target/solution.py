"""Find Smallest Letter Greater Than Target (LeetCode 744).

Given a non-decreasing list of lowercase letters and a target letter, return the
smallest letter strictly greater than target, wrapping around to letters[0] when
no such letter exists.
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """Return the smallest letter strictly greater than target (with wraparound).

        Args:
            letters: Lowercase letters sorted in non-decreasing order (length >= 2).
            target: A single lowercase letter to compare against.

        Returns:
            The smallest letter in `letters` that is strictly greater than
            `target`; if none exists, `letters[0]`.

        Example:
            >>> Solution().nextGreatestLetter(['c', 'f', 'j'], 'c')
            'f'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreatestLetter(['c', 'f', 'j'], 'a'))            # expected: 'c'
    print(sol.nextGreatestLetter(['c', 'f', 'j'], 'c'))            # expected: 'f'
    print(sol.nextGreatestLetter(['x', 'x', 'y', 'y'], 'z'))       # expected: 'x'
