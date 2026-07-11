# Sort Colors — Solution

## Brute Force

**Counting sort in two passes.** Count how many 0s, 1s, and 2s appear, then overwrite
the array with that many of each value in order.

```python
c0 = nums.count(0); c1 = nums.count(1)
nums[:] = [0] * c0 + [1] * c1 + [2] * (len(nums) - c0 - c1)
```

- **Time:** O(n) (two passes).
- **Space:** O(1) extra.

This is correct and fast, but it reads the data twice and is not the "single-pass,
partition" answer the problem is really testing.

## Optimal Approach (3-way partition / Dutch National Flag)

This is the partitioning core of Quick Sort specialized to a pivot value of `1`. We
keep three regions and one scanning pointer, and finish in **one pass**:

- `nums[0 .. low-1]` are all `0` (the `< pivot` region).
- `nums[low .. mid-1]` are all `1` (the `== pivot` region).
- `nums[mid .. high]` is **unexamined**.
- `nums[high+1 .. n-1]` are all `2` (the `> pivot` region).

Scan with `mid`:

- `nums[mid] == 0`: swap into the 0s region — `swap(low, mid)`, then `low++`, `mid++`.
  (The element swapped back from `low` is a known `1`, already scanned, so `mid`
  advances.)
- `nums[mid] == 1`: it is already in place — just `mid++`.
- `nums[mid] == 2`: swap into the 2s region — `swap(mid, high)`, then `high--`.
  Do **not** advance `mid`, because the value swapped in from `high` is unexamined.

Stop when `mid > high`.

### Why it is correct

The three region invariants above hold before and after every step. When `mid > high`
the unexamined region is empty, so all 0s are in `[0, low)`, all 1s in `[low, mid)`,
and all 2s in `(high, n)`, which is exactly red-white-blue order.

### Reference implementation

```python
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
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

### Complexity

- **Time:** O(n) — each element is inspected O(1) times; `mid` and `high` together
  advance across the array once.
- **Space:** O(1) — three index variables, sorted fully in place.

## Key Insights & Edge Cases

- The subtle rule is **not advancing `mid` on a `2`-swap**: the incoming element from
  `high` has not been classified yet, so it must be re-examined.
- On a `0`-swap, `mid` *can* advance because the element pulled from `low` is either a
  `1` (already scanned and in the middle region) or the same cell as `mid`.
- **Edge cases:** single element (`[0]`), all identical (`[1,1,1]`), and already sorted
  (`[0,1,2]`) all fall out of the invariants with no special casing.
- Generalizing the pivot from `1` to an arbitrary value turns this into the **3-way
  Quick Sort partition**, which keeps sorting at O(n log n) even when the input is
  dominated by duplicate keys.
