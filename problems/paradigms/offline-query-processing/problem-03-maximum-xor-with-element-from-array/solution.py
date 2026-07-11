from typing import List


class Solution:
    def maximizeXor(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        """Answer each query with the max XOR of ``x`` against a capped subset.

        For query ``[x_i, m_i]`` the answer is ``max(nums[j] XOR x_i)`` over all
        ``j`` with ``nums[j] <= m_i``, or ``-1`` if no element satisfies the cap.
        Answers are returned in the original order of ``queries``.

        Args:
            nums: A list of non-negative integers, each in ``[0, 10**9]``.
                Length up to ``10**5``.
            queries: A list of ``[x_i, m_i]`` pairs, each value in
                ``[0, 10**9]``. Length up to ``10**5``. Not sorted.

        Returns:
            A list ``answer`` where ``answer[i]`` is the maximum XOR for the
            ``i``-th query, or ``-1`` when every element exceeds ``m_i``.

        Example:
            >>> Solution().maximizeXor(
            ...     [0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]
            ... )
            [3, 3, 7]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.maximizeXor([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]])
    )  # expected: [3, 3, 7]
    print(
        sol.maximizeXor([5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]])
    )  # expected: [15, -1, 5]
