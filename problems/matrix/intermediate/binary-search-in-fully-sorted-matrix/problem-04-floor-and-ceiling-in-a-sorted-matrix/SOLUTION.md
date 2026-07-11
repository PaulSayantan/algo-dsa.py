# Solution — Floor and Ceiling in a Sorted Matrix

## Brute Force

Scan every value, tracking the best floor (largest `<= target`) and best ceil
(smallest `>= target`).

```python
floor, ceil = -1, -1
for row in matrix:
    for value in row:
        if value <= target and (floor == -1 or value > floor):
            floor = value
        if value >= target and (ceil == -1 or value < ceil):
            ceil = value
return [floor, ceil]
```

- **Time:** `O(m * n)`.
- **Space:** `O(1)`.

## Optimal Approach — Binary Search in a Fully-Sorted Matrix

Work on the virtual sorted array `A[idx] = matrix[idx // n][idx % n]` of length
`m * n`. Compute a single `lower_bound`:

```
pos = lower_bound(target)   # first flat index with A[pos] >= target
```

`pos` cleanly splits the array so both answers read off it:

- **Ceiling** = the smallest value `>= target`. That is `A[pos]` — *unless*
  `pos == m*n`, meaning every element is `< target`, in which case ceil = `-1`.
- **Floor** = the largest value `<= target`.
  - If `pos < m*n` and `A[pos] == target`, then `target` itself is present, so
    floor = `A[pos]` (= ceil = target).
  - Otherwise the floor is the element just before `pos`: `A[pos - 1]`, provided
    `pos > 0`. If `pos == 0`, every element is `> target`, so floor = `-1`.

**Algorithm.**

1. `m, n = len(matrix), len(matrix[0])`; `total = m * n`.
2. `pos = lower_bound(target)` via half-open binary search.
3. Compute `ceil`:
   - `ceil = A[pos]` if `pos < total` else `-1`.
4. Compute `floor`:
   - If `pos < total` and `A[pos] == target`: `floor = target`.
   - Else if `pos > 0`: `floor = A[pos - 1]`.
   - Else: `floor = -1`.
5. Return `[floor, ceil]`.

```python
class Solution:
    def floorAndCeil(self, matrix: List[List[int]], target: int) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        total = m * n

        def val(idx: int) -> int:
            return matrix[idx // n][idx % n]

        # lower_bound: first idx with val(idx) >= target
        lo, hi = 0, total
        while lo < hi:
            mid = (lo + hi) // 2
            if val(mid) < target:
                lo = mid + 1
            else:
                hi = mid
        pos = lo

        ceil = val(pos) if pos < total else -1
        if pos < total and val(pos) == target:
            floor = target
        elif pos > 0:
            floor = val(pos - 1)
        else:
            floor = -1
        return [floor, ceil]
```

**Why it is correct.** `lower_bound` partitions the array into a (possibly empty)
prefix of values `< target` and a suffix of values `>= target`. The last element
of the prefix is the floor (largest value not exceeding `target`) whenever
`target` is not itself present; the first element of the suffix is the ceil. When
`target` is present, `A[pos] == target` serves as both. The boundary cases
`pos == 0` and `pos == total` correspond exactly to "no floor" and "no ceil".

- **Time:** `O(log(m * n))`.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **One binary search yields both answers.** Because floor and ceil straddle the
  `lower_bound` split point, a single search suffices — no need to run separate
  floor and ceil searches.
- **Distinguish `pos == total` vs `pos == 0`.** The former means no ceiling
  exists (target beyond the max); the latter means no floor exists (target below
  the min). Return `-1` for the missing side.
- **Exact hit.** When `A[pos] == target`, floor and ceil are both `target`; do not
  accidentally take `A[pos - 1]` as the floor in that case.
- **Sentinel caveat.** This variant uses `-1` to mean "no such value." If your
  data can legitimately contain `-1`, return `None`/`Optional[int]` instead so the
  sentinel is unambiguous.
- **Mapping constant.** As always, `idx // n` and `idx % n` use the column count
  `n`.
