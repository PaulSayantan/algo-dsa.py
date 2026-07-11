"""Course Schedule IV.

LeetCode 1462. Solve with a boolean Floyd–Warshall transitive closure.
"""

from typing import List


class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        """Answer, for each query, whether u is a (direct or indirect) prerequisite of v.

        Build a boolean reachability matrix ``reach[u][v]`` = "u must be taken before v",
        seed it from the direct prerequisites, then close it transitively with the
        Floyd–Warshall triple loop using boolean OR/AND. Each query is a matrix lookup.

        Args:
            numCourses: Number of courses, labeled ``0 .. numCourses - 1``.
            prerequisites: List of ``[a, b]`` meaning a is a direct prerequisite of b.
            queries: List of ``[u, v]`` questions to answer.

        Returns:
            A list of booleans, one per query, where entry j is True iff ``queries[j][0]``
            is a prerequisite of ``queries[j][1]``.

        Example:
            >>> Solution().checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]])
            [False, True]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]))
    # Expected: [False, True]
    print(sol.checkIfPrerequisite(3, [[0, 1], [1, 2]], [[0, 2], [2, 0]]))
    # Expected: [True, False]
    print(
        sol.checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]])
    )
    # Expected: [True, True]
