# Solution — Minimum Value to Get Positive Step-by-Step Sum

## Brute Force

Try candidate `startValue` values `1, 2, 3, ...`. For each candidate, simulate
the whole step-by-step sum and check it never drops below 1; return the first
candidate that passes.

```python
start = 1
while True:
    total = start
    ok = True
    for x in nums:
        total += x
        if total < 1:
            ok = False
            break
    if ok:
        return start
    start += 1
```

- **Time:** O(n * A) where `A` is the answer's magnitude (up to ~10^4 given the
  constraints), because we resimulate the array for every candidate.
- **Space:** O(1).

## Optimal Approach (Running Minimum of Prefix Sums)

The step-by-step sum after processing the first `k` elements is
`startValue + (nums[0] + ... + nums[k-1])` = `startValue + prefix[k]`. The
constraint "never less than 1" must hold at *every* prefix, so it is binding at
the **smallest** prefix sum:

```
startValue + min_prefix >= 1   =>   startValue >= 1 - min_prefix
```

Since `startValue` must also be positive, the answer is
`max(1, 1 - min_prefix)`. We only need the running minimum of the prefix sums,
which one pass computes.

Reference implementation:

```python
def minStartValue(nums):
    running = 0
    min_prefix = 0          # the empty prefix has sum 0
    for x in nums:
        running += x
        min_prefix = min(min_prefix, running)
    return 1 - min_prefix   # equals max(1, 1 - min_prefix) since min_prefix <= 0
```

**Why it is correct.** The running total at any point equals
`startValue + prefix[k]` for some `k`. Its minimum over all `k` is
`startValue + min_prefix`. Requiring the minimum to be `>= 1` is *necessary and
sufficient* for all steps to be `>= 1`. Solving for the smallest such integer
gives `startValue = 1 - min_prefix`. Seeding `min_prefix = 0` accounts for the
empty prefix (before adding anything), which guarantees `min_prefix <= 0` and
therefore `1 - min_prefix >= 1`, so we never return a non-positive value and the
explicit `max(1, ...)` is unnecessary.

**Step-by-step** on `[-3, 2, -3, 4, 2]`:

| step | x | running (prefix sum) | min_prefix |
| ---- | -- | ------------------- | ---------- |
| init | – | 0                   | 0          |
| 1 | -3 | -3 | -3 |
| 2 |  2 | -1 | -3 |
| 3 | -3 | -4 | -4 |
| 4 |  4 |  0 | -4 |
| 5 |  2 |  2 | -4 |

`min_prefix = -4`, so `startValue = 1 - (-4) = 5`. Correct.

- **Time:** O(n) — single pass.
- **Space:** O(1).

## Key Insights & Edge Cases

- The only feature of the array that matters is its *most negative running
  prefix*. Everything else is irrelevant to the answer.
- Seed `min_prefix` with `0`, not `+infinity`: the running total before any
  element is exactly `startValue`, corresponding to prefix sum `0`. This also
  handles all-positive arrays (`[1, 2]`): `min_prefix` stays `0`, answer `1`.
- All-negative arrays push `min_prefix` down to the total sum; the answer grows
  accordingly.
- Because the answer must be positive, `1 - min_prefix` with `min_prefix <= 0`
  is automatically `>= 1`; no clamping needed.
