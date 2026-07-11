# Solution — Corporate Flight Bookings

## Brute Force

For each booking, walk every flight in `[first, last]` and add `seats`.

```python
def corpFlightBookings(bookings, n):
    answer = [0] * n
    for first, last, seats in bookings:
        for f in range(first, last + 1):   # 1-indexed flight numbers
            answer[f - 1] += seats
    return answer
```

- **Time:** `O(B * n)` where `B = len(bookings)`. With both up to `2 * 10^4`
  this is up to `4 * 10^8` operations — borderline-to-too-slow.
- **Space:** `O(n)` for the output.

## Optimal Approach (Difference Array)

Every booking is a range increment: add `seats` to flights `first .. last`.
Record the two boundary deltas into a difference array instead of touching the
whole range. Work in 0-indexed space (flight `f` -> index `f - 1`):

```
diff[first - 1] += seats     # seats start counting at flight `first`
diff[last]      -= seats     # index `last` == (last - 1) + 1, i.e. one past the end
```

Note `last` (0-indexed) is exactly one position past flight `last`'s index
`last - 1`, so the subtraction cancels the increment right after the range ends.
Then prefix-sum to get per-flight totals.

```python
def corpFlightBookings(bookings, n):
    diff = [0] * (n + 1)               # sentinel slot so diff[last] is always valid
    for first, last, seats in bookings:
        diff[first - 1] += seats
        diff[last]      -= seats       # one past the 0-indexed end
    answer = [0] * n
    running = 0
    for i in range(n):
        running += diff[i]
        answer[i] = running
    return answer
```

- **Time:** `O(B + n)`.
- **Space:** `O(n)`.

**Why it is correct:** summing bookings over each flight is a sum of range
increments. The difference array records each range as a `+seats` / `-seats`
boundary pair, and the prefix sum reverses the difference to yield, at each
flight, the total of all increments whose range covers it — identical to the
brute-force result.

## Key Insights & Edge Cases

- **1-indexed vs 0-indexed.** The only subtlety here is the index shift. Flight
  `first` maps to `diff[first - 1]`, and "one past flight `last`" maps to
  `diff[last]` (because flight `last` sits at index `last - 1`). Getting this
  mapping right is the whole game.
- **Sentinel size.** `diff` has length `n + 1` so that when `last == n` the write
  `diff[last] = diff[n]` stays in bounds and is harmlessly ignored.
- **Single-flight bookings** (`first == last`) still work: `+seats` at
  `first - 1` and `-seats` at `first` net out to affecting exactly one flight.
- **Large seat counts** sum without overflow in Python; in fixed-width languages
  use 64-bit integers since totals can reach `B * max_seats`.
