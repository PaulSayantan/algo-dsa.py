# Rank Transform of an Array — Solution

## Brute Force

For each element, count how many **distinct** values are strictly smaller than it; that
count plus one is the rank.

```python
def arrayRankTransform(arr):
    distinct = sorted(set(arr))
    result = []
    for x in arr:
        # count distinct values strictly less than x
        rank = sum(1 for v in distinct if v < x) + 1
        result.append(rank)
    return result
```

- **Time:** `O(n)` per element to scan `distinct`, so `O(n^2)` overall (plus the sort).
- **Space:** `O(n)` for the distinct set.

This is quadratic and times out for `n = 10^5`.

## Optimal Approach (Coordinate Compression)

The rank of a value is *exactly* its 1-based index in the sorted list of distinct values.
That is coordinate compression with a `+1` offset. Build a `value -> rank` map once, then
answer every element in `O(1)`.

```python
def arrayRankTransform(arr):
    rank = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
    return [rank[x] for x in arr]
```

**Why it is correct.**

- `sorted(set(arr))` lists the distinct values in increasing order, so a larger value gets
  a strictly larger index — satisfying "larger element, larger rank."
- `set` collapses duplicates to one entry, so equal values map to the same rank.
- Consecutive indices `0, 1, 2, ...` (shifted to `1, 2, 3, ...`) contain no gaps, giving the
  smallest possible ranks.

**Step by step** on `[37, 12, 28, 9, 100, 56, 80, 5, 12]`:

1. `set` -> `{5, 9, 12, 28, 37, 56, 80, 100}`.
2. `sorted` -> `[5, 9, 12, 28, 37, 56, 80, 100]`.
3. Map -> `{5:1, 9:2, 12:3, 28:4, 37:5, 56:6, 80:7, 100:8}`.
4. Look up each original element -> `[5, 3, 4, 2, 8, 6, 7, 1, 3]`.

- **Time:** `O(n log n)` for the sort, then `O(n)` lookups. Dominated by the sort.
- **Space:** `O(n)` for the map and output.

## Key Insights & Edge Cases

- **Empty array** must return `[]`; the dict-comprehension handles this naturally.
- **All-equal array** (`[100, 100, 100]`) collapses to a single distinct value -> every rank
  is `1`.
- **Duplicates get identical ranks** because `set` deduplicates before ranking; do not use
  the raw sorted array (with duplicates) or you would create gaps.
- The huge value range (`-10^9 .. 10^9`) is irrelevant — only the *order* matters, which is
  the whole point of coordinate compression.
- Using a hash map makes lookups `O(1)`; an alternative is `bisect_left(distinct, x) + 1`,
  which is `O(log n)` per lookup and avoids building the dict.
