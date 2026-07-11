from typing import List


class Solution:
    def countShifts(self, nums: List[int]) -> int:
        """Count the total shifts insertion sort performs to sort ``nums``.

        A shift is one inner-loop move ``nums[j+1] = nums[j]``. Placing the key
        into its final gap does not count. This total equals the number of
        inversions (pairs i < j with nums[i] > nums[j]) in the array.

        Args:
            nums: Integers to (conceptually) sort. 1 <= len(nums) <= 1e4.

        Returns:
            The total number of shifts / inversions as an int (can be up to
            n*(n-1)/2).

        Example:
            >>> Solution().countShifts([2, 4, 1, 3, 5])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countShifts([2, 4, 1, 3, 5]))  # expected: 3
    print(sol.countShifts([3, 2, 1]))        # expected: 3
    print(sol.countShifts([1, 2, 3, 4]))     # expected: 0
