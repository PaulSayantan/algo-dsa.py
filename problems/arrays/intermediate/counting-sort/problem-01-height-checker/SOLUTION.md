# Height Checker — Solution

## Brute Force

Make a copy of `heights`, sort the copy with a general comparison sort, then walk both arrays
in lockstep counting mismatches.

```python
def heightChecker(heights):
    expected = sorted(heights)
    return sum(a != b for a, b in zip(heights, expected))
```

- **Time:** `O(n log n)` for the comparison sort.
- **Space:** `O(n)` for the sorted copy.

This is perfectly acceptable given the tiny constraints, but it ignores the fact that the
values live in a fixed, tiny range — which is exactly the signal to use counting sort.

## Optimal Approach (Counting Sort)

Heights are integers in `[1, 100]`, so we can sort in linear time without any comparisons.

**Steps:**

1. Allocate `count` of size `101` (indices `0..100`) initialized to zero.
2. **Count phase:** for each `h` in `heights`, increment `count[h]`. Now `count[v]` is exactly
   how many students have height `v`.
3. **Rebuild + compare phase:** walk `v` from `1` to `100`. For each `v`, "emit" it `count[v]`
   times. Each emitted value is the next entry of the sorted `expected` array, so compare it
   against `heights[i]` at the running index `i`; increment a `result` counter on mismatch and
   advance `i`.

Because we compare on the fly, we never even materialize the `expected` array — the count
array *is* the sorted sequence in compressed form.

```python
def heightChecker(heights):
    count = [0] * 101
    for h in heights:
        count[h] += 1

    result = 0
    i = 0
    for v in range(1, 101):
        while count[v] > 0:
            if heights[i] != v:
                result += 1
            count[v] -= 1
            i += 1
    return result
```

**Why it is correct:** Reading the counts in increasing value order reproduces exactly the
non-decreasing sorted array, position for position. Comparing each reconstructed value with
the original element at the same index therefore counts precisely the out-of-place students.

- **Time:** `O(n + k)` where `k = 100`. The count loop is `O(n)`; the rebuild loop touches
  each of the `k` buckets and emits `n` values total, so `O(n + k)`.
- **Space:** `O(k)` for the fixed 101-slot count array.

## Key Insights & Edge Cases

- **No output array needed.** The count array holds the sorted order implicitly; you can
  compare against the original as you decompress it.
- **Index alignment.** The running index `i` must advance once per emitted value (mismatch or
  not), so it stays in lockstep with the sorted position.
- **Already-sorted input** returns `0` — every emitted value matches the original.
- **Duplicates** are handled naturally; counting sort thrives on repeated keys.
- **1-based values.** Heights start at 1, so index `0` of the count array simply stays unused;
  sizing the array to `max+1 = 101` avoids off-by-one errors.
