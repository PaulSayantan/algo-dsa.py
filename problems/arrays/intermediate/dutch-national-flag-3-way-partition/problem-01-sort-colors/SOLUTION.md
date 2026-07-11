# Sort Colors — Solution

## Brute Force

**Counting sort (two passes).** Count how many 0s, 1s, and 2s appear, then overwrite the
array with that many 0s, then 1s, then 2s.

```python
def sortColors(nums):
    c = [0, 0, 0]
    for x in nums:
        c[x] += 1
    i = 0
    for val in (0, 1, 2):
        for _ in range(c[val]):
            nums[i] = val
            i += 1
```

- **Time:** O(n) — two passes over the data.
- **Space:** O(1) — a fixed 3-slot counter.

This is perfectly correct and O(n), but it reads the array twice. The follow-up asks for a
**one-pass, in-place** solution, which is exactly what Dutch National Flag delivers.

## Optimal Approach — Dutch National Flag

Use the pivot value `1` and three pointers:

- `low` — everything in `nums[0 .. low-1]` is a confirmed `0`.
- `mid` — the current scanning index; `nums[low .. mid-1]` are confirmed `1`s.
- `high` — everything in `nums[high+1 .. n-1]` is a confirmed `2`.
- `nums[mid .. high]` is the unexamined region.

Process while `mid <= high`:

1. `nums[mid] == 0`: swap into the low region — `swap(low, mid)`, then `low += 1; mid += 1`.
   (The element pulled from `low` is either a `1` we already passed or equals `mid`, so
   advancing `mid` is safe.)
2. `nums[mid] == 1`: it belongs in the middle; just `mid += 1`.
3. `nums[mid] == 2`: swap into the high region — `swap(mid, high)`, then `high -= 1`. Do
   **not** advance `mid`, because the value swapped in from `high` has not been examined.

```python
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```

### Why it is correct

The invariants `nums[0..low-1] == 0`, `nums[low..mid-1] == 1`, and `nums[high+1..] == 2`
hold before and after every iteration. Each iteration either advances `mid` (cases 0 and 1)
or shrinks `high` (case 2), so the unexamined gap `high - mid` strictly decreases and the
loop terminates. When `mid > high` the unexamined region is empty and all three invariants
cover the whole array, so it is fully sorted.

### Worked trace on `[2,0,2,1,1,0]`

| low | mid | high | array | action |
|-----|-----|------|-------|--------|
| 0 | 0 | 5 | `[2,0,2,1,1,0]` | nums[mid]=2 → swap(0,5), high=4 |
| 0 | 0 | 4 | `[0,0,2,1,1,2]` | nums[mid]=0 → swap(0,0), low=1, mid=1 |
| 1 | 1 | 4 | `[0,0,2,1,1,2]` | nums[mid]=0 → swap(1,1), low=2, mid=2 |
| 2 | 2 | 4 | `[0,0,2,1,1,2]` | nums[mid]=2 → swap(2,4), high=3 |
| 2 | 2 | 3 | `[0,0,1,1,2,2]` | nums[mid]=1 → mid=3 |
| 2 | 3 | 3 | `[0,0,1,1,2,2]` | nums[mid]=1 → mid=4 |
| 2 | 4 | 3 | `[0,0,1,1,2,2]` | mid>high, stop |

Result: `[0,0,1,1,2,2]`.

- **Time:** O(n) — one pass, each step advances `mid` or lowers `high`.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Do not advance `mid` after the `2`-swap.** The incoming element from `high` is unknown
  and must be re-examined; advancing `mid` here is the most common bug.
- **Loop condition is `mid <= high` (inclusive).** With `mid < high` you skip inspecting the
  final unexamined element.
- After a `0`-swap, advancing `mid` is safe because `low <= mid`, so the element received
  from index `low` was already processed (it can only be a `1`).
- Edge cases: single element, all-same arrays (`[0,0,0]`), already sorted, and
  reverse-sorted all work without special casing.
- Generalizes directly to any pivot: replace the `== 0 / == 1 / == 2` tests with
  `< pivot / == pivot / > pivot`.
