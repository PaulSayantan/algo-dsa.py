from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """Decide whether all trips can be served without exceeding capacity.

        Each trip [numPassengers, from, to] boards `numPassengers` riders at
        kilometer `from` who get off at kilometer `to`. The car only drives east.

        Args:
            trips: A list of [numPassengers, from, to] trips.
            capacity: The maximum number of passengers the car can hold at once.

        Returns:
            True if occupancy never exceeds `capacity` at any point, else False.

        Example:
            >>> Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4)
            False
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.carPooling([[2, 1, 5], [3, 3, 7]], 4))  # expected: False
    print(sol.carPooling([[2, 1, 5], [3, 3, 7]], 5))  # expected: True
