# Subarray Sum Equals K — Solution

## Brute Force

Consider every start index `i` and extend a running sum to each end index `j`,
counting whenever it hits `k`.

```python
count = 0
for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total += nums[j]
        if total == k:
            count += 1
return count
```

- **Time:** O(n^2) — a running sum for every start avoids a third loop but there are
  still O(n^2) (start, end) pairs.
- **Space:** O(1).

Note a sliding window is **not** applicable here: negative numbers mean the sum is
not monotonic as the window grows, so you cannot decide to shrink or grow. We need
a different idea.

## Optimal Approach (Hashing)

Let `prefix[t]` be the sum of the first `t` elements, so the sum of the subarray
`nums[i..j]` equals `prefix[j+1] - prefix[i]`. This subarray sums to `k` exactly
when:

```
prefix[j+1] - prefix[i] == k   <=>   prefix[i] == prefix[j+1] - k
```

So while scanning left to right and maintaining the current prefix sum `cur`, the
number of subarrays ending at the current position that sum to `k` equals the
number of earlier prefix sums equal to `cur - k`. Keep a hash map `freq` from a
prefix-sum value to how many times it has occurred so far.

```python
from collections import defaultdict

def subarraySum(nums, k):
    freq = defaultdict(int)
    freq[0] = 1            # empty prefix: enables subarrays starting at index 0
    cur = 0
    count = 0
    for x in nums:
        cur += x
        count += freq[cur - k]   # earlier prefixes that complete a sum of k
        freq[cur] += 1           # record current prefix for future indices
    return count
```

**Why it is correct.** Before processing position `j`, `freq[v]` holds the number
of indices `i <= j` (as prefix boundaries) whose prefix sum is `v`. When we reach
`cur = prefix[j+1]`, every earlier boundary `i` with `prefix[i] == cur - k` yields
a distinct subarray `nums[i..j]` summing to `k`, and there are exactly `freq[cur-k]`
of them. Summing this over all `j` counts every qualifying subarray once. The
seed `freq[0] = 1` represents the empty prefix, correctly counting subarrays that
begin at index 0 (whose prefix sum itself equals `k`).

- **Time:** O(n) — one pass, O(1) average map operations.
- **Space:** O(n) — up to n distinct prefix sums.

### Trace on `nums = [1, 1, 1], k = 2`

| x | cur | need = cur-k | freq[need] | count | freq after |
|---|-----|--------------|-----------|-------|------------|
| — | 0   | —            | —         | 0     | {0:1} |
| 1 | 1   | -1           | 0         | 0     | {0:1, 1:1} |
| 1 | 2   | 0            | 1         | 1     | {0:1, 1:1, 2:1} |
| 1 | 3   | 1            | 1         | 2     | {0:1, 1:1, 2:1, 3:1} |

Final count = 2, matching the expected output.

## Key Insights & Edge Cases

- **Seed `freq[0] = 1`.** Without it you miss every subarray that starts at index 0
  and sums to `k`.
- **Count, then insert.** Update `count += freq[cur - k]` *before* incrementing
  `freq[cur]`, so a zero-length subarray is never counted at the current step.
- **Negatives / zeros** are handled naturally — this is the reason we use prefix
  sums plus a map instead of a sliding window.
- **Store frequencies, not just presence.** Repeated prefix sums (common with
  zeros or `[1, -1, 1, -1]`) each contribute, so the map value must be a count.
- **Overlapping subarrays** are counted independently, as required.
