from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Return the 1-indexed positions of the two numbers that sum to target.

        The input array `numbers` is sorted in non-decreasing order and is
        guaranteed to contain exactly one valid pair. Only constant extra space
        may be used.

        Args:
            numbers: A 1-indexed (conceptually) list of integers sorted in
                non-decreasing order.
            target: The integer sum the two chosen numbers must equal.

        Returns:
            A list ``[index1, index2]`` of two 1-indexed positions with
            ``1 <= index1 < index2 <= len(numbers)`` such that
            ``numbers[index1 - 1] + numbers[index2 - 1] == target``.

        Example:
            >>> Solution().twoSum([2, 7, 11, 15], 9)
            [1, 2]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # expected: [1, 2]
    print(sol.twoSum([2, 3, 4], 6))       # expected: [1, 3]
    print(sol.twoSum([-1, 0], -1))        # expected: [1, 2]
