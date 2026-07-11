# Relative Sort Array — Solution

## Brute Force

Use a custom comparator. Build a rank map from `arr2` (value -> its index). Sort `arr1` with a
key that returns the rank if the value is in `arr2`, otherwise a large sentinel plus the value
itself so unranked elements sort ascending after all ranked ones.

```python
def relativeSortArray(arr1, arr2):
    rank = {v: i for i, v in enumerate(arr2)}
    big = len(arr2)
    return sorted(arr1, key=lambda x: (rank.get(x, big), x if x not in rank else 0))
```

- **Time:** `O(n log n)` for the comparison sort.
- **Space:** `O(n)` for the rank map and output.

Correct, but it relies on comparisons even though the values are tightly bounded.

## Optimal Approach (Counting Sort)

Every value in `arr1` is in `[0, 1000]`, so tally frequencies and emit them in the exact order
we want. The output ordering is fully under our control because counting sort lets us decide
the traversal order over buckets.

**Steps:**

1. Build `count[0..1000]` where `count[v]` is the number of times `v` appears in `arr1`.
2. **First, honor `arr2`'s order.** For each value `v` in `arr2`, append `v` to the result
   `count[v]` times, then set `count[v] = 0` so it is not emitted again.
3. **Then, append leftovers ascending.** Sweep `v` from `0` to `1000`; any remaining
   `count[v] > 0` are values not in `arr2`, so append each `v` that many times. Sweeping in
   increasing `v` guarantees ascending order for the tail.

```python
def relativeSortArray(arr1, arr2):
    count = [0] * 1001
    for v in arr1:
        count[v] += 1

    result = []
    for v in arr2:            # phase A: follow arr2's order
        result.extend([v] * count[v])
        count[v] = 0
    for v in range(1001):     # phase B: leftovers in ascending order
        if count[v] > 0:
            result.extend([v] * count[v])
    return result
```

**Why it is correct:** Phase A places every value named in `arr2` in `arr2`'s order with the
right multiplicity, then zeroes those buckets so they cannot be double-counted. Phase B scans
buckets in increasing value, which emits exactly the values absent from `arr2` in ascending
order. Together they use each occurrence of each value exactly once.

- **Time:** `O(n + k)` with `k = 1000`. Counting is `O(n)`; both emission phases together
  produce `n` elements and scan `k` buckets.
- **Space:** `O(k)` for the count array plus `O(n)` for the output.

## Key Insights & Edge Cases

- **Traversal order = sort order.** The power of counting sort here is that we choose the
  bucket-visiting order (arr2 first, then ascending), so a "custom sort" becomes two linear
  passes.
- **Zeroing after phase A** is essential; otherwise values in `arr2` would be emitted again
  during the ascending sweep.
- **Duplicates in arr1** are handled directly by the counts.
- **Values equal to 0** are valid keys — sizing the array to `1001` covers index `0..1000`.
- Because `arr2` is guaranteed distinct and a subset of `arr1`, no bucket is visited twice in
  phase A and no `arr2` value is missing.
