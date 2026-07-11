"""Next Greater Element II — LeetCode 503.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """Find the next greater number for each element of a circular array.

        Traversal wraps from the last element back to the first. The next greater
        number of ``nums[i]`` is the first strictly greater value reachable by
        moving forward (with wrap-around); ``-1`` if none exists.

        Args:
            nums: A circular list of integers.

        Returns:
            A list ``res`` where ``res[i]`` is the next greater number of
            ``nums[i]`` in circular order, or ``-1`` if there is none.

        Example:
            >>> Solution().nextGreaterElements([1, 2, 1])
            [2, -1, 2]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElements([1, 2, 1]))        # expected: [2, -1, 2]
    print(sol.nextGreaterElements([1, 2, 3, 4, 3]))  # expected: [2, 3, 4, -1, 4]
    print(sol.nextGreaterElements([5, 4, 3, 2, 1]))  # expected: [-1, 5, 5, 5, 5]
