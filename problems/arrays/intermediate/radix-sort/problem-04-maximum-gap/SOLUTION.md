# Solution — Maximum Gap

## Brute Force

Sort the array with a comparison sort and scan adjacent pairs.

```python
def maximumGap(self, nums):
    if len(nums) < 2:
        return 0
    nums = sorted(nums)                       # O(n log n)
    return max(b - a for a, b in zip(nums, nums[1:]))
```

- **Time:** `O(n log n)` (comparison sort dominates)
- **Space:** `O(n)`

Correct, but it violates the problem's explicit **linear-time** requirement.

## Optimal Approach (Radix Sort + Linear Scan)

The values are bounded (`<= 10^9`), so we can replace the comparison sort with
an `O(n)` **LSD radix sort**, then take the maximum adjacent difference in one
pass.

```python
def maximumGap(self, nums):
    n = len(nums)
    if n < 2:
        return 0

    # LSD radix sort, base 2^16 -> at most 2 passes for values up to 10^9 < 2^30.
    BASE = 1 << 16
    MASK = BASE - 1
    mx = max(nums)
    arr = list(nums)
    shift = 0
    while (mx >> shift) > 0:
        count = [0] * (BASE + 1)
        for x in arr:
            count[((x >> shift) & MASK) + 1] += 1
        for i in range(1, BASE + 1):
            count[i] += count[i - 1]
        output = [0] * n
        for x in arr:                          # forward scan + start offsets = stable
            d = (x >> shift) & MASK
            output[count[d]] = x
            count[d] += 1
        arr = output
        shift += 16

    best = 0
    for i in range(1, n):
        best = max(best, arr[i] - arr[i - 1])
    return best
```

### Why it is correct

- Radix sort produces the fully sorted array (each stable counting-sort pass on
  a higher-order chunk preserves the order of the lower-order chunks; by
  induction the array is sorted after the last pass).
- The maximum gap of a sorted sequence is, by definition, the largest difference
  between consecutive elements, which the final linear scan computes directly.

### Complexity

With base `2^16`, values up to `10^9 < 2^30` need at most `d = 2` passes.

- **Time:** `O(d · (n + k))` with `d = 2`, `k = 2^16` → `O(n)` for large `n`.
- **Space:** `O(n + k)` — the output buffer plus the `2^16` count array.

### Alternative: Pigeonhole / bucket method

The canonical LeetCode 164 solution avoids sorting entirely. Spread the values
into `n - 1` buckets of width `ceil((max - min) / (n - 1))`. By the pigeonhole
principle at least one bucket is empty, so the maximum gap must occur **between**
buckets, not inside one. Track each bucket's min and max, then scan buckets
comparing the current bucket's min with the previous non-empty bucket's max.
This is also `O(n)` time / `O(n)` space and uses less constant overhead than a
`2^16`-radix sort. Both approaches are accepted; radix sort is the more direct
"sort then scan" realization of the linear-time requirement.

## Key Insights & Edge Cases

- **Fewer than 2 elements → return 0** (nothing to compare). Handle this before
  sorting.
- **All equal values** (e.g. `[1,1,1,1]`) → every adjacent difference is 0, so
  the answer is 0.
- **Bounded values are what unlock linearity.** If values were arbitrary-precision
  or `d` grew with `n`, radix sort would lose its linear-time edge and the bucket
  method (which depends only on the range, not digit count) would be preferable.
- **Base choice trade-off:** a bigger base means fewer passes but a larger count
  array; `2^16` keeps it to two passes for 30-bit values while staying memory
  reasonable.
- **Stability isn't strictly required for the final answer** (we only need the
  sorted order, and duplicates are indistinguishable), but the stable
  formulation is what makes the multi-pass radix sort correct.
