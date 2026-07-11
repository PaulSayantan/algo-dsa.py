# Solution — Subarray Sums Divisible by K

## Brute Force

Enumerate every start `i` and end `j`, accumulate the sum, and count when it is
divisible by `k`.

```python
count = 0
for i in range(len(nums)):
    running = 0
    for j in range(i, len(nums)):
        running += nums[j]
        if running % k == 0:
            count += 1
return count
```

- **Time:** O(n^2).
- **Space:** O(1).

## Optimal Approach — Prefix Sum + Hash Map (remainder counts)

`sum(nums[i+1..j]) = prefix[j] - prefix[i]` is divisible by `k` **iff**
`prefix[j] % k == prefix[i] % k`. So group prefix sums by their remainder mod
`k`. For each new prefix, the number of valid subarrays ending here equals how
many *previous* prefixes share its remainder.

Keep a hash map `count[r]` = number of prefixes seen so far with remainder `r`,
seeded with `{0: 1}` for the empty prefix. Normalize the remainder to
`0 .. k-1` so negatives are handled (`((running % k) + k) % k`, though Python's
`%` already returns a non-negative result for positive `k`).

```python
from collections import defaultdict

def subarraysDivByK(nums, k):
    count = defaultdict(int)
    count[0] = 1
    running = 0
    total = 0
    for x in nums:
        running = (running + x) % k     # Python % keeps this in 0..k-1
        total += count[running]         # pair with earlier same-remainder prefixes
        count[running] += 1
    return total
```

### Why it is correct

- Every earlier prefix with the same remainder as the current one forms a
  subarray (ending at the current index) whose sum is a multiple of `k`.
- Adding `count[running]` before incrementing it counts exactly the earlier
  occurrences (non-empty subarrays), and the `{0: 1}` seed accounts for
  subarrays that start at index 0.
- Equivalently, if a remainder `r` occurs `c` times across all prefixes
  (including the seed), it contributes `C(c, 2) = c*(c-1)/2` subarrays.

### Step by step on `nums = [4, 5, 0, -2, -3, 1], k = 5`

Prefix sums: 4, 9, 9, 7, 4, 5. Remainders mod 5: 4, 4, 4, 2, 4, 0.

| x  | running%5 | count[r] before | total | count after |
|----|-----------|-----------------|-------|-------------|
| —  | 0 (seed)  | —               | 0     | {0:1}       |
| 4  | 4         | 0               | 0     | {0:1, 4:1}  |
| 5  | 4         | 1               | 1     | {0:1, 4:2}  |
| 0  | 4         | 2               | 3     | {0:1, 4:3}  |
| -2 | 2         | 0               | 3     | {..., 2:1}  |
| -3 | 4         | 3               | 6     | {0:1, 4:4, 2:1} |
| 1  | 0         | 1               | 7     | {0:2, 4:4, 2:1} |

Result: **7** ✓.

- **Time:** O(n).
- **Space:** O(min(n, k)) — at most `k` distinct remainders.

## Key Insights & Edge Cases

- **Normalize negative remainders.** In languages where `%` can return a
  negative value (C++, Java), use `((running % k) + k) % k`. Python's `%`
  already yields `0 .. k-1` for positive `k`, but writing the normalization
  makes the intent explicit and portable.
- **Seed `{0: 1}`** so prefixes that are themselves divisible by `k` are
  counted.
- **Counts, not indices** — this counts *all* qualifying subarrays, so store how
  many prefixes hit each remainder (the combinatorial `C(c, 2)` view).
- **`k >= 2` is guaranteed**, so `% k` is always well defined.
