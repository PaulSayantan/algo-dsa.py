from typing import List


class Solution:
    def elementsMoreThanNOverK(self, nums: List[int], k: int) -> List[int]:
        """Return all distinct elements appearing more than floor(n/k) times.

        At most k-1 such elements can exist. Use the k-1 candidate
        generalization of Boyer–Moore voting (Misra–Gries) for the first pass,
        then verify each surviving candidate with a real count. Aim for O(n*k)
        time and O(k) extra space.

        Args:
            nums: A non-empty list of integers.
            k: An integer >= 2; the divisor in the floor(n/k) threshold.

        Returns:
            A list of the (at most k-1) qualifying elements, each once, in any
            order.

        Example:
            >>> sorted(Solution().elementsMoreThanNOverK([3, 1, 2, 2, 1, 2, 3, 3], 4))
            [2, 3]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    s = Solution()

    print(sorted(s.elementsMoreThanNOverK([3, 1, 2, 2, 1, 2, 3, 3], 4)))  # expected: [2, 3]
    print(s.elementsMoreThanNOverK([1, 1, 1, 1], 3))                      # expected: [1]
    print(s.elementsMoreThanNOverK([1, 2, 3, 4, 5], 2))                   # expected: []
