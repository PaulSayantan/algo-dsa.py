"""Car Pooling (LeetCode 1094).

Fill in `Solution.carPooling` using a 1D sweep line over weighted events.
This file is an intentionally empty template — no working solution is provided.
"""

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """Decide whether all trips fit without ever exceeding capacity.

        Each trip [n, frm, to] occupies n seats over the half-open interval
        [frm, to). Emit a +n event at frm and a -n event at to, sweep the events
        in location order carrying a running sum of onboard passengers, and check
        that the sum never exceeds `capacity`. Drop-offs at a location must be
        applied before pickups at the same location.

        Args:
            trips: List of [numPassengers, from, to] bookings.
            capacity: Number of seats in the car.

        Returns:
            True if every trip can be served without the onboard count ever
            exceeding `capacity`, otherwise False.

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
    print(sol.carPooling([[2, 1, 5], [3, 5, 7]], 3))  # expected: True
