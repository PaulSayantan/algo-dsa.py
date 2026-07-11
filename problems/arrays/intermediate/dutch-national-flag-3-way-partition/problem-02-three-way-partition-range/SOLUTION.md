# Three-Way Partition Around a Range — Solution

## Brute Force

**Stable bucketing with an auxiliary array.** Make one pass collecting elements `< lowVal`,
a second pass collecting elements in `[lowVal, highVal]`, and a third for elements
`> highVal`; concatenate and copy back.

```python
def threeWayPartition(arr, lowVal, highVal):
    less   = [x for x in arr if x < lowVal]
    middle = [x for x in arr if lowVal <= x <= highVal]
    more   = [x for x in arr if x > highVal]
    arr[:] = less + middle + more
    return arr
```

- **Time:** O(n).
- **Space:** O(n) for the three buckets.

Correct, but it allocates a second array. The point of this problem is to achieve the same
grouping **in place** and in **one pass**.

## Optimal Approach — Dutch National Flag with a Range

This is the DNF algorithm where the single pivot is replaced by a range test. Categories:

- `arr[i] < lowVal`  → belongs to the low region.
- `lowVal <= arr[i] <= highVal` → belongs to the middle region.
- `arr[i] > highVal` → belongs to the high region.

Pointers:

- `low` — `arr[0 .. low-1]` are all `< lowVal`.
- `mid` — scanner; `arr[low .. mid-1]` are all in range.
- `high` — `arr[high+1 .. n-1]` are all `> highVal`.

```python
def threeWayPartition(arr, lowVal, highVal):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] < lowVal:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > highVal:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:  # lowVal <= arr[mid] <= highVal
            mid += 1
    return arr
```

### Why it is correct

Same invariants as classic DNF. Elements confirmed low sit left of `low`, in-range elements
sit between `low` and `mid`, and elements confirmed high sit right of `high`. Every iteration
either advances `mid` (low-swap or in-range) or lowers `high` (high-swap), so `high - mid`
strictly shrinks and the loop ends. After the `> highVal` swap we keep `mid` fixed because
the value pulled from `high` is unexamined.

### Worked trace on `arr = [1, 4, 2, -2, 5, 8, 0]`, `lowVal = 2`, `highVal = 5`

| low | mid | high | array | action |
|-----|-----|------|-------|--------|
| 0 | 0 | 6 | `[1,4,2,-2,5,8,0]` | 1<2 → swap(0,0), low=1, mid=1 |
| 1 | 1 | 6 | `[1,4,2,-2,5,8,0]` | 4 in [2,5] → mid=2 |
| 1 | 2 | 6 | `[1,4,2,-2,5,8,0]` | 2 in [2,5] → mid=3 |
| 1 | 3 | 6 | `[1,4,2,-2,5,8,0]` | -2<2 → swap(1,3), low=2, mid=4 |
| 2 | 4 | 6 | `[1,-2,2,4,5,8,0]` | 5 in [2,5] → mid=5 |
| 2 | 5 | 6 | `[1,-2,2,4,5,8,0]` | 8>5 → swap(5,6), high=5 |
| 2 | 5 | 5 | `[1,-2,2,4,5,0,8]` | 0<2 → swap(2,5), low=3, mid=6 |
| 3 | 6 | 5 | `[1,-2,0,4,5,2,8]` | mid>high, stop |

Result: `[1, -2, 0, 4, 5, 2, 8]` → region membership `< 2` = `{1,-2,0}`, in `[2,5]` =
`{4,5,2}`, `> 5` = `{8}`. A valid three-way partition (internal order differs from Example 2,
which is fine — any valid grouping is accepted).

- **Time:** O(n).
- **Space:** O(1).

## Key Insights & Edge Cases

- The output is **not unique**: only the three-region grouping is graded, not the order
  inside each region. DNF and the bucket method may produce different (both valid) arrays.
- When `lowVal == highVal`, the middle region collapses to a single value and this reduces to
  the classic single-pivot DNF.
- Watch the pointer discipline: advance `mid` on a low-swap and on in-range; keep `mid` fixed
  on a high-swap.
- Degenerate inputs (all elements below the range, all in range, all above, single element)
  need no special handling.
- Duplicates equal to `lowVal` or `highVal` are inclusive and land in the middle region.
