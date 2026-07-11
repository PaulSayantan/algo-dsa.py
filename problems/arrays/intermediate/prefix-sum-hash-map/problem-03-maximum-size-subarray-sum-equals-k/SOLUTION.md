# Solution — Maximum Size Subarray Sum Equals k

## Brute Force

Try every start index `i`, extend the end `j`, keep a running sum, and record
the length whenever the running sum hits `k`.

```python
best = 0
for i in range(len(nums)):
    running = 0
    for j in range(i, len(nums)):
        running += nums[j]
        if running == k:
            best = max(best, j - i + 1)
return best
```

- **Time:** O(n^2).
- **Space:** O(1).

## Optimal Approach — Prefix Sum + Hash Map

With `prefix[j] = nums[0] + ... + nums[j]`, the subarray `nums[i+1..j]` sums to
`k` exactly when `prefix[j] - prefix[i] = k`, i.e. `prefix[i] = prefix[j] - k`.

Because we want the **longest** such subarray, we want the **smallest** index
`i` whose prefix sum equals `prefix[j] - k`. So we store, for each prefix-sum
value, the **first (earliest) index** where it occurred, and never overwrite
it. Seed with `{0: -1}` for the empty prefix.

```python
def maxSubArrayLen(nums, k):
    first_index = {0: -1}   # prefix sum 0 before index 0
    running = 0
    best = 0
    for i, x in enumerate(nums):
        running += x
        if running - k in first_index:
            best = max(best, i - first_index[running - k])
        if running not in first_index:
            first_index[running] = i   # keep earliest index only
    return best
```

### Why it is correct

- When `running - k` exists in the map at index `p`, the subarray
  `nums[p+1..i]` sums to `k` and has length `i - p`. Using the earliest `p`
  maximizes that length.
- We must check the map **before** possibly inserting `running`, and we insert
  only if the value is absent, so `first_index` always holds the leftmost
  occurrence.

### Step by step on `nums = [1, -1, 5, -2, 3], k = 3`

| i | x  | running | need = running-3 | in map @ | best | map insert |
|---|----|---------|------------------|----------|------|------------|
| — | —  | 0       | —                | —        | 0    | {0:-1}     |
| 0 | 1  | 1       | -2               | no       | 0    | +{1:0}     |
| 1 | -1 | 0       | -3               | no       | 0    | 0 exists   |
| 2 | 5  | 5       | 2                | no       | 0    | +{5:2}     |
| 3 | -2 | 3       | 0                | yes @ -1 | 3-(-1)=4 | +{3:3} |
| 4 | 3  | 6       | 3                | yes @ 3  | max(4, 4-3)=4 | +{6:4} |

Result: **4** ✓ (subarray `[1, -1, 5, -2]`).

- **Time:** O(n).
- **Space:** O(n).

## Key Insights & Edge Cases

- **Earliest index, not count.** This is the "longest subarray" flavor of the
  technique — mirror image of LeetCode 560, which stores counts.
- **Do not overwrite** an existing prefix-sum entry; the first occurrence gives
  the widest reach.
- **Seed `{0: -1}`** so a qualifying prefix `nums[0..i]` yields length
  `i - (-1) = i + 1`.
- **Negative numbers and zeros** are handled naturally; a sliding window would
  fail because the running sum is not monotonic.
- If no subarray sums to `k`, the map lookups never succeed and the function
  returns `0`.
