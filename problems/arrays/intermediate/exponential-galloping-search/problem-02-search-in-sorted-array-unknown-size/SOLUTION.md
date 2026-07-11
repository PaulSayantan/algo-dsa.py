# Solution — Search in a Sorted Array of Unknown Size

## Brute Force

Walk indices `0, 1, 2, ...` calling `reader.get(i)` until the value equals
`target` (return `i`), exceeds `target` (return `-1`, since the array is sorted
and unique), or hits the out-of-bounds sentinel `2^31 - 1` (return `-1`).

```python
def search(reader, target):
    i = 0
    while True:
        v = reader.get(i)
        if v == target:
            return i
        if v > target:          # sentinel or a genuinely larger element
            return -1
        i += 1
```

- **Time:** `O(k)` where `k` is the position of the answer (or of the first
  element `> target`). Worst case `O(n)`.
- **Space:** `O(1)`.

Correct, but linear — it defeats the purpose of a sorted array.

## Optimal Approach (Exponential / Galloping Search)

The obstacle to a plain binary search is that we have no `hi`. Exponential
search **manufactures** one. The out-of-bounds sentinel `2^31 - 1` is larger
than any real element and larger than any valid `target` (`target <= 10^4`), so
it behaves exactly like "we walked off the end and the value is too big" — the
doubling loop treats it identically to a real element that overshoots.

**Phase 1 — gallop to find the bound.** Start at `bound = 1` and double while
`reader.get(bound) < target`. When the loop stops, `reader.get(bound) >= target`
(either a real element `>= target`, or the sentinel meaning past-the-end).

**Phase 2 — binary search `[bound // 2, bound]`.** Every index below
`bound // 2` was confirmed `< target`, and `bound` reaches or exceeds it, so the
answer (if any) is inside this window. Compare `reader.get(mid)` — sentinels for
out-of-bounds `mid` compare as "too big," pushing `hi` left correctly.

```python
def search(reader, target):
    # Phase 1: find a bound whose value is >= target (sentinel counts as "big").
    bound = 1
    while reader.get(bound) < target:
        bound *= 2

    # Phase 2: binary search in [bound // 2, bound].
    lo, hi = bound // 2, bound
    while lo <= hi:
        mid = (lo + hi) // 2
        v = reader.get(mid)
        if v == target:
            return mid
        if v < target:
            lo = mid + 1
        else:                   # v > target, including the sentinel
            hi = mid - 1
    return -1
```

**Why is it correct?** Uniqueness means there is at most one match. The doubling
invariant ("all indices `< bound` are `< target`") guarantees the answer is not
left of `bound // 2`. Since `reader.get(bound) >= target`, the answer is not
right of `bound`. Inside the window, out-of-bounds reads return the sentinel,
which is `> target`, so the binary search shrinks `hi` past the real end without
ever mistaking padding for a match.

- **Time:** `O(log k)` where `k` is the answer's index — `O(ceil(log2 k))` reads
  to find the bound plus `O(log k)` for the binary search. This is `<= O(log n)`.
- **Space:** `O(1)`.

### Step-by-step on `secret = [-1,0,3,5,9,12], target = 9`

| phase | bound / mid | get(...) | action |
|-------|-------------|----------|--------|
| gallop | 1 | 0 | `0 < 9` -> double |
| gallop | 2 | 3 | `3 < 9` -> double |
| gallop | 4 | 9 | `9 >= 9` -> stop; window = [2, 4] |
| binary | mid = 3 | 5 | `5 < 9` -> lo = 4 |
| binary | mid = 4 | 9 | `9 == 9` -> return 4 |

## Key Insights & Edge Cases

- **The sentinel is the trick.** Because `2^31 - 1 > target` always, you never
  need a separate "am I out of bounds?" branch — comparisons handle it.
- **Start the gallop at index 1, not 0.** Index 0 is the natural `lo` of the
  first window (`bound // 2 == 0`), and the binary search will examine it.
- **Single-element array (`n == 1`):** `get(1)` returns the sentinel `>= target`,
  so the loop stops immediately with `bound = 1` and window `[0, 1]`; binary
  search checks index 0 (real) and index 1 (sentinel). Correct.
- **Target smaller than everything:** the loop stops at `bound = 1` (since
  `get(1) >= target` is likely, or it never enters if `get(1) >= target`), and
  binary search over `[0, 1]` returns `-1`.
- **Overflow is a non-issue in Python** (arbitrary precision ints), but in
  fixed-width languages, cap `bound` or use `bound = min(bound * 2, someCap)` to
  avoid signed overflow when doubling.
- **Uniqueness** is what lets Phase 2 stop at the first match; with duplicates
  you would switch to a lower-bound search (see Problem 4).
