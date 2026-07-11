# Solution — Sort Records by Date

## Brute Force

Build a single comparison key per record — e.g. `key = (year, month, day)` — and
run an `O(n log n)` comparison sort (or Python's `sorted`). This works and is
even stable, but it is a comparison sort and does not illustrate (or exploit)
the bounded-field structure.

- **Time:** `O(n log n)`
- **Space:** `O(n)`

## Optimal Approach (Multi-Key Radix Sort)

This is the *original* radix sort idea (sorting punch cards column by column).
Each field is a bounded integer, so we run a **stable counting sort** on one
field at a time, from **least significant to most significant**:

1. Stable counting sort by **day** (`1..31`).
2. Stable counting sort by **month** (`1..12`).
3. Stable counting sort by **year** (`1900..2100`, offset by 1900 → `0..200`).

```python
def _counting_sort_by(records, key, k):
    # key: record -> integer in [0, k); stable
    count = [0] * (k + 1)
    for r in records:
        count[key(r) + 1] += 1
    for i in range(1, k + 1):        # prefix sums -> start offsets
        count[i] += count[i - 1]
    output = [None] * len(records)
    for r in records:                # forward scan + start offsets = stable
        c = key(r)
        output[count[c]] = r
        count[c] += 1
    return output

def sort_records_by_date(records):
    arr = list(records)
    arr = _counting_sort_by(arr, lambda r: r[0] - 1, 31)          # day 1..31
    arr = _counting_sort_by(arr, lambda r: r[1] - 1, 12)          # month 1..12
    arr = _counting_sort_by(arr, lambda r: r[2] - 1900, 201)      # year 1900..2100
    return arr
```

### Why it is correct

The key invariant of radix sort: **sort by the least significant key first,
using a stable sort at every step.** When we later sort by a more significant
key, records that tie on that key retain the order imposed by the previous
passes. So after the final pass on `year`:

- Records are grouped by year (most significant).
- Within a year, ties were broken by the earlier month pass.
- Within a (year, month) group, ties were broken by the earliest day pass.

That is precisely `(year, month, day)` ascending order, and identical dates keep
their input order because every pass is stable.

### Complexity

Let `n` be the number of records. The three passes have radices `31`, `12`, and
`201`.

- **Time:** `O(n + 31) + O(n + 12) + O(n + 201) = O(n)` (constant number of
  passes, each with a bounded radix).
- **Space:** `O(n)` for the output buffer (plus `O(k)` for each pass's count
  array, bounded by ~201).

## Key Insights & Edge Cases

- **Pass order is non-negotiable:** you *must* go day → month → year. Reversing
  the order (year first, day last) would produce records sorted by day, which is
  wrong.
- **Every pass must be stable.** If any single field sort were unstable, ties on
  a more significant field could be reordered incorrectly.
- **Offsetting the year** (`year - 1900`) keeps the count array small (201 slots)
  instead of indexing by the raw year value.
- **Duplicates / identical dates:** preserved in input order by stability
  (Example 3).
- **Single record / empty input:** returned unchanged; each pass is a no-op.
- **Alternative:** you could pack the date into one integer
  (`year*10000 + month*100 + day`) and run a standard LSD integer radix sort; the
  multi-field version shown here avoids the arithmetic and makes the stability
  argument explicit.
