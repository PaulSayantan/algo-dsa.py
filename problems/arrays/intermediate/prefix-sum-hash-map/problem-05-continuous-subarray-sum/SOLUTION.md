# Solution — Continuous Subarray Sum

## Brute Force

Try every start `i` and every end `j >= i + 1` (to guarantee length >= 2),
accumulate the sum, and check divisibility by `k`.

```python
for i in range(len(nums)):
    running = nums[i]
    for j in range(i + 1, len(nums)):
        running += nums[j]
        if running % k == 0:
            return True
return False
```

- **Time:** O(n^2).
- **Space:** O(1).

## Optimal Approach — Prefix Sum + Hash Map (on remainders)

The sum of `nums[i+1..j]` is `prefix[j] - prefix[i]`. This is a multiple of `k`
**iff** `prefix[j] % k == prefix[i] % k` — the two prefix sums share the same
remainder modulo `k`.

So track the running prefix-sum **remainder** `running % k`. Keep a hash map
from each remainder to the **earliest index** where it appeared, seeded with
`{0: -1}` (empty prefix has remainder 0 at virtual index `-1`). When the current
remainder was seen before at index `p`, the subarray `nums[p+1..i]` has length
`i - p` and a sum divisible by `k`. Require `i - p >= 2`.

```python
def checkSubarraySum(nums, k):
    first_index = {0: -1}   # remainder 0 before index 0
    running = 0
    for i, x in enumerate(nums):
        running = (running + x) % k
        if running in first_index:
            if i - first_index[running] >= 2:
                return True
            # else: keep the earlier index, do NOT overwrite
        else:
            first_index[running] = i
    return False
```

### Why it is correct

- Equal remainders => difference of the two prefix sums is a multiple of `k`.
- Storing the **earliest** index for each remainder maximizes the index gap, so
  if *any* qualifying subarray exists for that remainder, the earliest pairing
  finds it (the gap only grows). We therefore never overwrite an existing entry.
- The seed `{0: -1}` lets a prefix `nums[0..i]` that is itself divisible by `k`
  be detected with length `i - (-1) = i + 1 >= 2` for `i >= 1`.

### Step by step on `nums = [23, 2, 4, 6, 7], k = 6`

| i | x  | running%6 | seen @ | gap check | map insert |
|---|----|-----------|--------|-----------|------------|
| — | —  | 0         | seed   | —         | {0:-1}     |
| 0 | 23 | 23%6=5    | no     | —         | +{5:0}     |
| 1 | 2  | (5+2)%6=1 | no     | —         | +{1:1}     |
| 2 | 4  | (1+4)%6=5 | yes @0 | 2-0=2 ✓   | return True |

Result: **True** ✓ (subarray `[2, 4]` sums to 6).

- **Time:** O(n).
- **Space:** O(min(n, k)) — at most `k` distinct remainders.

## Key Insights & Edge Cases

- **Key on the remainder, not the raw sum.** This is the modular twist on the
  prefix-sum + hash-map pattern.
- **Length constraint (>= 2)** is enforced by the `i - p >= 2` check and the
  `{0: -1}` seed; do not overwrite a remainder's stored index, or you would
  shorten the gap and miss valid answers.
- **Sum of 0 counts** as a multiple of `k` (n = 0). For example `[0, 0]` with
  any `k` returns `True`, because both prefixes have remainder 0 two indices
  apart.
- **`k` is guaranteed positive** by the constraints, so `% k` is well defined;
  if a variant allowed `k = 0` you would fall back to searching for two equal
  raw prefix sums (a zero-sum subarray).
