"""Maximum Compatibility Score Sum (LeetCode 1947) — empty solution template.

Build a score matrix, then use the Hungarian Algorithm to maximize the total
compatibility (minimize the negated score). Do NOT hard-code answers.
"""

from typing import List


class Solution:
    def maxCompatibilitySum(
        self, students: List[List[int]], mentors: List[List[int]]
    ) -> int:
        """Return the maximum total compatibility score over all pairings.

        Args:
            students: ``m`` answer arrays, each of length ``n`` with values in
                ``{0, 1}``.
            mentors: ``m`` answer arrays, each of length ``n`` with values in
                ``{0, 1}``.

        Returns:
            The maximum achievable sum of compatibility scores when each student
            is matched to exactly one mentor (and vice versa). The compatibility
            of a pair is the count of positions where their answers agree.

        Example:
            >>> Solution().maxCompatibilitySum(
            ...     [[1, 1, 0], [1, 0, 1], [0, 0, 1]],
            ...     [[1, 0, 0], [0, 0, 1], [1, 1, 0]])
            8
        """
        # TODO: implement.
        #   1) build score[i][j] = number of matching answers
        #   2) run Hungarian on the negated score matrix
        #   3) return the negated minimum
        pass


if __name__ == "__main__":
    students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
    mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
    print(Solution().maxCompatibilitySum(students, mentors))  # Expected: 8
