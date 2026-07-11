# Corporate Flight Bookings

**Difficulty:** Medium

**Source:** LeetCode 1109 — Corporate Flight Bookings

## Description

There are `n` flights numbered from `1` to `n`.

You are given an array `bookings` where `bookings[i] = [first_i, last_i, seats_i]`
represents a booking for `seats_i` seats reserved on **each** flight in the
inclusive range from flight `first_i` to flight `last_i`.

Return an array `answer` of length `n`, where `answer[j]` is the total number of
seats reserved for flight `j + 1` (i.e. `answer` is 0-indexed while flights are
1-indexed).

## Constraints

- `1 <= n <= 2 * 10^4`
- `1 <= bookings.length <= 2 * 10^4`
- `bookings[i].length == 3`
- `1 <= first_i <= last_i <= n`
- `1 <= seats_i <= 10^4`

## Examples

### Example 1

```
Input:  n = 5, bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
Output: [10, 55, 45, 25, 25]
```

**Explanation:** Consider the seats reserved per flight (1-indexed):
- Flight 1: 10 (from booking 1) = 10
- Flight 2: 10 + 20 + 25 = 55
- Flight 3: 20 + 25 = 45
- Flight 4: 25
- Flight 5: 25

So the answer is `[10, 55, 45, 25, 25]`.

### Example 2

```
Input:  n = 2, bookings = [[1, 2, 10], [2, 2, 15]]
Output: [10, 25]
```

**Explanation:**
- Flight 1: 10 (from the first booking only) = 10
- Flight 2: 10 (first booking) + 15 (second booking) = 25

So the answer is `[10, 25]`.

## Hint

Each booking adds a constant to a contiguous range of flights. Rather than
touching every flight in the range, mark `+seats` at the range start and
`-seats` just past the range end using a **Difference Array**, then prefix-sum.
