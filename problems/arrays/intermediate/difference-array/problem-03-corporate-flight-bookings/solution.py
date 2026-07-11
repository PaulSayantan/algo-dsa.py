from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """Total the seats reserved for each of n flights across all bookings.

        Each booking [first, last, seats] reserves `seats` seats on every flight
        in the inclusive 1-indexed range [first, last].

        Args:
            bookings: A list of [first, last, seats] reservations. Flights are
                numbered from 1 to n.
            n: The number of flights.

        Returns:
            A 0-indexed list of length n where entry j is the total seats
            reserved on flight j + 1.

        Example:
            >>> Solution().corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5)
            [10, 55, 45, 25, 25]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))  # expected: [10, 55, 45, 25, 25]
    print(sol.corpFlightBookings([[1, 2, 10], [2, 2, 15]], 2))              # expected: [10, 25]
