from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Rotate ``nums`` to the right by ``k`` steps, in place.

        Args:
            nums: The list of integers to rotate. Modified in place.
            k: The number of positions to rotate right (may exceed len(nums)).

        Returns:
            None. The rotation is performed by mutating ``nums`` directly.

        Example:
            >>> data = [1, 2, 3, 4, 5, 6, 7]
            >>> Solution().rotate(data, 3)
            >>> data
            [5, 6, 7, 1, 2, 3, 4]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(data, 3)
    print(data)  # expected: [5, 6, 7, 1, 2, 3, 4]
