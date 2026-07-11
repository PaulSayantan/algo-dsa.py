from typing import List


class Solution:
    def maximumBeauty(
        self, items: List[List[int]], queries: List[int]
    ) -> List[int]:
        """Return the max beauty of any item priced at most each query's budget.

        For each ``queries[j]``, the answer is the maximum ``beauty`` over all
        items whose ``price <= queries[j]``, or ``0`` when no item qualifies.
        Answers must be returned in the original order of ``queries``.

        Args:
            items: A list of ``[price, beauty]`` pairs, each value in
                ``[1, 10**9]``. Length up to ``10**5``.
            queries: A list of budgets, each in ``[1, 10**9]``. Length up to
                ``10**5``. Not sorted.

        Returns:
            A list ``answer`` of the same length as ``queries`` where
            ``answer[j]`` is the maximum beauty affordable under ``queries[j]``.

        Example:
            >>> Solution().maximumBeauty(
            ...     [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]
            ... )
            [2, 4, 5, 5, 6, 6]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.maximumBeauty(
            [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]
        )
    )  # expected: [2, 4, 5, 5, 6, 6]
    print(sol.maximumBeauty([[1, 2], [1, 2], [1, 3], [1, 4]], [1]))  # expected: [4]
    print(sol.maximumBeauty([[10, 1000]], [5]))  # expected: [0]
