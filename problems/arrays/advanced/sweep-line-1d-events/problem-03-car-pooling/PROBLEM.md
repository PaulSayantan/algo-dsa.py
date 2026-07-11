# Car Pooling

**Difficulty:** Medium

**Source:** LeetCode 1094 — "Car Pooling"

## Description

A car with `capacity` empty seats drives east along a straight road, making only
forward trips (it never turns around). You are given a list `trips` where
`trips[i] = [numPassengers_i, from_i, to_i]` means the `i`-th booking picks up
`numPassengers_i` people at location `from_i` and drops them off at location
`to_i`. A passenger occupies a seat on the half-open interval `[from_i, to_i)` —
passengers are dropped off *before* the car reaches `to_i`, so a booking that
drops off at location `x` frees its seats for another booking that picks up at
`x`.

Return `true` if and only if it is possible to pick up and drop off all
passengers for every trip so that the number of people in the car **never
exceeds `capacity`** at any point along the road.

## Constraints

- `1 <= trips.length <= 1000`
- `1 <= numPassengers_i <= 100`
- `0 <= from_i < to_i <= 1000`
- `1 <= capacity <= 10^5`

## Examples

### Example 1

```
Input:  trips = [[2, 1, 5], [3, 3, 7]], capacity = 4
Output: false
Explanation:
  On the segment [3, 5) both bookings are aboard: 2 + 3 = 5 passengers,
  which exceeds the capacity of 4. So it is not possible.
```

### Example 2

```
Input:  trips = [[2, 1, 5], [3, 3, 7]], capacity = 5
Output: true
Explanation:
  The peak load on [3, 5) is 2 + 3 = 5, exactly equal to the capacity of 5.
  Never exceeding capacity, so the trips are feasible.
```

### Example 3

```
Input:  trips = [[2, 1, 5], [3, 5, 7]], capacity = 3
Output: true
Explanation:
  The first booking drops off at location 5, exactly where the second picks up.
  Because occupancy is half-open [from, to), the 2 seats are freed before the
  3 new passengers board, so the peak load is only 3 <= 3. Feasible.
```

## Hint

This is a **weighted** version of the overlap counter. Emit a `+numPassengers`
event at each `from` and a `-numPassengers` event at each `to`, then run a
**Sweep Line (1D events)** that carries a running **sum** of onboard passengers.
The trip set is feasible exactly when that running sum never exceeds `capacity`.
Order events so that a drop-off at a location is applied before a pickup at the
same location.
