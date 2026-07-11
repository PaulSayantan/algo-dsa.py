from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Remove duplicates in place from a sorted array and return the count.

        After the call, the first ``k`` positions of ``nums`` hold the unique
        values in their original order, where ``k`` is the returned value.
        Elements beyond index ``k`` are unspecified. Uses O(1) extra memory.

        Args:
            nums: A list of integers sorted in non-decreasing order. Mutated in
                place.

        Returns:
            The number ``k`` of unique elements now stored in ``nums[:k]``.

        Example:
            >>> nums = [1, 1, 2]
            >>> Solution().removeDuplicates(nums)
            2
            >>> nums[:2]
            [1, 2]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    a = [1, 1, 2]
    k = sol.removeDuplicates(a)
    print(k, a[:k] if k else a)  # expected: 2 [1, 2]

    b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = sol.removeDuplicates(b)
    print(k, b[:k] if k else b)  # expected: 5 [0, 1, 2, 3, 4]

    c = [5]
    k = sol.removeDuplicates(c)
    print(k, c[:k] if k else c)  # expected: 1 [5]
