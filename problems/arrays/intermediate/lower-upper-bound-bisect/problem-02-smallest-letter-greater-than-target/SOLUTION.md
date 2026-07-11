# Solution — Find Smallest Letter Greater Than Target

## Brute Force

Scan left to right; return the first letter strictly greater than `target`. If the scan finishes
without finding one, return `letters[0]`.

```python
def nextGreatestLetter(letters, target):
    for c in letters:
        if c > target:
            return c
    return letters[0]
```

- **Time:** `O(n)`.
- **Space:** `O(1)`.

Correct, but linear — it ignores the sorted structure.

## Optimal Approach — Upper Bound (bisect) with wraparound

"Smallest letter **strictly greater** than target" is exactly the element at the **upper bound**
index of `target`. The upper bound is the first index whose value is `> target`:

```python
def nextGreatestLetter(letters, target):
    lo, hi = 0, len(letters)       # hi exclusive; answer index in [0, n]
    while lo < hi:
        mid = (lo + hi) // 2
        if letters[mid] <= target: # <= : skip everything not strictly greater
            lo = mid + 1
        else:                      # letters[mid] > target -> candidate; keep, look left
            hi = mid
    return letters[lo % len(letters)]   # wrap: lo == n means "none greater" -> index 0
```

### Why it is correct

**Invariant:** every index in `[0, lo)` holds a letter `<= target`, and every index in `[hi, n)`
holds a letter `> target`. The loop shrinks `[lo, hi)` until empty; `lo` ends as the first index
with a letter strictly greater than `target`.

- The comparison is `<=` (not `<`). That is what makes this the **upper** bound: a letter equal to
  `target` is treated as "not greater", so we move past it. This is why `target = 'c'` on
  `['c','f','j']` returns `'f'` and not `'c'`.
- If every letter is `<= target`, the loop ends with `lo == n`. Then `lo % n == 0`, so we return
  `letters[0]` — exactly the required wraparound behavior.

### Step-by-step on `letters = ['c','f','j'], target = 'c'`

| lo | hi | mid | letters[mid] | comparison  | action |
|----|----|-----|--------------|-------------|--------|
| 0  | 3  | 1   | 'f'          | `'f' > 'c'` | hi = 1 |
| 0  | 1  | 0   | 'c'          | `'c' <= 'c'`| lo = 1 |
| 1  | 1  | —   | —            | loop ends   | return `letters[1 % 3]` = `'f'` |

- **Time:** `O(log n)`.
- **Space:** `O(1)`.

Standard library equivalent: `letters[bisect.bisect_right(letters, target) % len(letters)]`.

## Key Insights & Edge Cases

- **Upper vs lower bound** is the whole point: "strictly greater" ⇒ upper bound (`<=` in the test).
  If the problem had asked for "greater than or equal", you would use lower bound (`<`).
- **The `% len(letters)` trick** elegantly folds the "no answer, wrap to front" case into the same
  return statement — no special-casing needed.
- **Target below everything** (Example 1) → upper bound is `0` → returns `letters[0]`, which happens
  to be both the wrap answer and the genuine answer; both agree.
- **Duplicates** (Example 3, `['x','x','y','y']`) are handled naturally; upper bound skips the entire
  run of letters `<= target`.
- Comparing single-character Python strings with `<`, `<=`, `>` compares them by code point, which
  matches alphabetical order for lowercase letters — no conversion to integers needed.
