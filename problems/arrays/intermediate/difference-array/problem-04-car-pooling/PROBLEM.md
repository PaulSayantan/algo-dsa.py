# Car Pooling

**Difficulty:** Medium

**Source:** LeetCode 1094 — Car Pooling

## Description

There is a car with `capacity` empty seats. The vehicle only drives east (i.e.
it cannot turn around and drive west).

You are given the integer `capacity` and an array `trips` where
`trips[i] = [numPassengers_i, from_i, to_i]` indicates that the `i`-th trip has
`numPassengers_i` passengers who board at location `from_i` and get off at
location `to_i`. The locations are given as the number of kilometers due east
from the car's initial location.

Return `true` if it is possible to pick up and drop off all passengers for all
the given trips **without ever exceeding** the car's `capacity`, and `false`
otherwise.

## Constraints

- `1 <= trips.length <= 1000`
- `trips[i].length == 3`
- `1 <= numPassengers_i <= 100`
- `0 <= from_i < to_i <= 1000`
- `1 <= capacity <= 10^5`

## Examples

### Example 1

```
Input:  trips = [[2, 1, 5], [3, 3, 7]], capacity = 4
Output: false
```

**Explanation:** Between kilometers 3 and 5 both trips overlap, so the car holds
`2 + 3 = 5` passengers, which exceeds the capacity of 4. Therefore it is
impossible, and the answer is `false`.

### Example 2

```
Input:  trips = [[2, 1, 5], [3, 3, 7]], capacity = 5
Output: true
```

**Explanation:** The peak occupancy is again `5` passengers (km 3 to 5), but now
capacity is 5, which is exactly enough. At no point does occupancy exceed 5, so
the answer is `true`.

## Hint

Passengers occupy the interval `[from, to)` — they leave exactly at `to`. Add
`+numPassengers` at `from` and `-numPassengers` at `to` in a **Difference
Array** over kilometers, then prefix-sum and check that the running occupancy
never exceeds `capacity`.
