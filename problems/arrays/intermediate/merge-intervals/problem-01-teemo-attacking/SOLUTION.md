# Teemo Attacking — Solution

## Brute Force

Simulate every poisoned second. Keep a set of poisoned seconds; for each attack
`t`, add every integer in `[t, t + duration)` to the set. The answer is the size
of the set.

- **Time:** `O(n * duration)` — for each of the `n` attacks we may insert up to
  `duration` seconds.
- **Space:** `O(total seconds)` for the set.

With `duration` up to `10^7` and `n` up to `10^4`, this is far too slow and
memory-hungry. We should never actually enumerate individual seconds.

## Optimal Approach (Merge Intervals)

Each attack at `t` creates the half-open interval `[t, t + duration)`. Since
`timeSeries` is already sorted in non-decreasing order, we can sweep once and
merge on the fly. For consecutive attacks `prev` and `cur`:

- The **gap** between two consecutive attacks is `cur - prev`.
- The previous window contributes `min(gap, duration)` fully-counted seconds:
  - If `cur - prev >= duration`, the previous window `[prev, prev + duration)`
    finished before the next attack, so it contributes its full `duration`.
  - If `cur - prev < duration`, the next attack **refreshes** the timer early, so
    the previous window only contributes `cur - prev` seconds before being reset.
- The **last** attack always contributes a full `duration`, because nothing
  follows it to cut it short.

```python
def findPoisonedDuration(timeSeries, duration):
    if not timeSeries:
        return 0
    total = 0
    for i in range(1, len(timeSeries)):
        gap = timeSeries[i] - timeSeries[i - 1]
        total += min(gap, duration)
    return total + duration  # the final attack always lasts the full duration
```

An equivalent explicit-merge formulation keeps a running window `[start, end)`
and, for each attack, either extends `end` (overlap) or closes the window and
adds its length to the total. Both are the same Merge Intervals sweep; the code
above just collapses it into a single arithmetic step per pair.

**Why it is correct:** because the attacks are sorted, any window that can
overlap window `i` must be window `i-1` or `i+1`. Comparing each adjacent pair
therefore captures every possible overlap, and `min(gap, duration)` is exactly
the non-overlapping contribution of each window.

- **Time:** `O(n)` (input already sorted; otherwise `O(n log n)` to sort).
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Half-open windows** `[t, t + duration)` are the natural model: an attack at
  `t = 3` with `duration = 2` covers seconds 3 and 4, i.e. length 2, and touches
  but does not include second 5.
- **`duration == 0`** means no poison at all; every `min(gap, 0)` term and the
  trailing `+ duration` are 0, so the answer is 0. The formula handles this
  automatically.
- **Duplicate attack times** (`gap == 0`) contribute `min(0, duration) = 0`,
  correctly avoiding double counting simultaneous attacks.
- **Single attack** returns exactly `duration` (the loop never runs).
- Watch for integer overflow in languages with fixed-width ints: `n * duration`
  can reach `10^4 * 10^7 = 10^11`. Python integers are unbounded, so this is only
  a concern when porting to, say, Java (`long`).
