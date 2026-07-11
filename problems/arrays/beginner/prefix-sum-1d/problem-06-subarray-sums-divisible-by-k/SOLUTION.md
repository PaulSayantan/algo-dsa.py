# Solution — Subarray Sums Divisible by K

## Brute Force

Enumerate every subarray, accumulate its sum, and test divisibility.

```python
def subarraysDivByK(nums, k):
    count = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total % k == 0:
                count += 1
    return count
```

- **Time:** O(n^2).
- **Space:** O(1).

With `n` up to `3 * 10^4` this is ~10^9 operations — too slow in practice.

## Optimal Approach (Prefix Sum, 1D + Remainder Counting)

The subarray covering indices `i .. j-1` has sum `prefix[j] - prefix[i]`. That
difference is divisible by `k` exactly when the two prefixes share the same
remainder modulo `k`:

```
(prefix[j] - prefix[i]) % k == 0   <=>   prefix[j] % k == prefix[i] % k
```

So sweep the running sum, reduce it mod `k`, and for each remainder count how
many earlier prefixes had that same remainder. Every earlier match forms a valid
subarray. Track remainder frequencies in a size-`k` table.

The one subtlety: in most languages (Python included) the `%` operator can yield
a **negative** remainder for negative operands, so normalize it into `[0, k)`
with `((running % k) + k) % k`.

Reference implementation:

```python
def subarraysDivByK(nums, k):
    counts = [0] * k
    counts[0] = 1          # empty prefix has remainder 0
    running = 0
    result = 0
    for x in nums:
        running += x
        r = ((running % k) + k) % k   # normalize to [0, k)
        result += counts[r]
        counts[r] += 1
    return result
```

**Why it is correct:** after processing element `j`, `running % k` is the
remainder of `prefix[j+1]`. Any earlier prefix with the same remainder `r`
produces a subarray whose sum is a multiple of `k`, so we add `counts[r]` (the
number of such earlier prefixes) before recording the current one. Seeding
`counts[0] = 1` represents the empty prefix and correctly counts subarrays that
start at index 0 and are themselves divisible by `k`.

**Step by step** on `nums = [4, 5, 0, -2, -3, 1]`, `k = 5`:

| x  | running | r = normalized mod 5 | counts[r] added | result | counts (index:value)      |
|----|---------|----------------------|-----------------|--------|---------------------------|
| -  | 0       | -                    | -               | 0      | {0:1}                      |
| 4  | 4       | 4                    | 0               | 0      | {0:1, 4:1}                 |
| 5  | 9       | 4                    | 1               | 1      | {0:1, 4:2}                 |
| 0  | 9       | 4                    | 2               | 3      | {0:1, 4:3}                 |
| -2 | 7       | 2                    | 0               | 3      | {0:1, 2:1, 4:3}            |
| -3 | 4       | 4                    | 3               | 6      | {0:1, 2:1, 4:4}            |
| 1  | 5       | 0                    | 1               | 7      | {0:2, 2:1, 4:4}            |

Final result = 7.

- **Time:** O(n) — single pass; the mod table is indexed in O(1).
- **Space:** O(k) for the remainder-count table.

## Key Insights & Edge Cases

- The reusable idea: "sum divisible by k" becomes "two prefixes with equal
  remainder mod k." This mirrors Subarray Sum Equals K, but the equivalence
  classes are remainders instead of exact values.
- **Normalize negative remainders.** `((running % k) + k) % k` is essential;
  skipping it splits what should be one class (e.g. `-1` and `k-1`) into two and
  undercounts. This is the number-one bug for this problem.
- **Seed the remainder-0 bucket with 1** for the empty prefix, so a prefix that
  is itself divisible by `k` is counted.
- **Count pairs, not booleans.** If a remainder appears `m` times, it
  contributes `C(m, 2)` subarrays; the incremental `result += counts[r]` before
  the increment accumulates exactly that.
- A fixed-size list of length `k` is faster than a hash map here because
  remainders are dense in `[0, k)`.
