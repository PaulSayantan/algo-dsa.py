# Solution — First 1 in an Infinite Sorted Binary Array

## Brute Force

Read indices `0, 1, 2, ...` until `reader.get(i) == 1`, and return `i`. Since
the array is eventually all `1`s, the loop always terminates.

```python
def first_one(reader):
    i = 0
    while reader.get(i) == 0:
        i += 1
    return i
```

- **Time:** `O(t)` where `t` is the index of the first `1` — linear in the
  answer position.
- **Space:** `O(1)`.

The transition is monotonic ("all `0`s then all `1`s"), so linear scanning
wastes the structure we could binary-search on.

## Optimal Approach (Exponential / Galloping Search)

"Is `bits[i] == 1`?" is a **monotonic predicate**: false for a prefix of indices,
then true forever after. Exponential search is the natural fit for an unbounded
monotonic predicate — find *any* index where it is true, then binary search for
the boundary.

**Phase 1 — gallop until we see a `1`.** Start with `bound = 1` and double while
`reader.get(bound) == 0`. Because the array is eventually all `1`s, this loop is
guaranteed to stop — at the first probe `1, 2, 4, 8, ...` that lands at or past
the transition `t`.

**Phase 2 — binary search `[bound // 2, bound]` for the leftmost `1`.** Every
index below `bound // 2` was confirmed `0` (that is why we doubled past it), and
`reader.get(bound) == 1`, so the transition lies in this window. Use a
leftmost-true binary search: whenever `get(mid) == 1`, record it and move `hi`
left to look for an earlier `1`.

```python
def first_one(reader):
    # Phase 1: gallop until a 1 appears.
    bound = 1
    while reader.get(bound) == 0:
        bound *= 2

    # Phase 2: leftmost-1 binary search over [bound // 2, bound].
    lo, hi = bound // 2, bound
    ans = bound                  # bound is known to be a 1, so it is a valid answer
    while lo <= hi:
        mid = (lo + hi) // 2
        if reader.get(mid) == 1:
            ans = mid            # candidate; keep searching left for an earlier 1
            hi = mid - 1
        else:
            lo = mid + 1
    return ans
```

**Why is it correct?** The doubling loop's invariant is "every index `< bound`
reads `0`," so the first `1` is not left of `bound // 2` (the previous probe).
Since `reader.get(bound) == 1`, the transition is at or before `bound`, inside
the window. The leftmost-true search then returns the *first* `1`, not an
arbitrary one. Seeding `ans = bound` is safe because `bound` itself is a proven
`1`.

**Why `O(log t)`?** If the answer sits at index `t`, doubling stops when `bound`
first reaches or exceeds `t`, i.e. after `ceil(log2 t)` steps, so `bound < 2t`.
The window handed to binary search has size `< t`, another `O(log t)`. Total:
`O(log t)`, versus `O(t)` for the linear scan.

- **Time:** `O(log t)` where `t` is the index of the first `1`.
- **Space:** `O(1)`.

### Step-by-step on `bits = 0,0,0,0,1,1,1,... (t = 4)`

| phase | bound / mid | get(...) | action |
|-------|-------------|----------|--------|
| gallop | 1 | 0 | double -> bound = 2 |
| gallop | 2 | 0 | double -> bound = 4 |
| gallop | 4 | 1 | stop; window = [2, 4] |
| binary | mid = 3 | 0 | lo = 4 |
| binary | mid = 4 | 1 | ans = 4, hi = 3 (loop ends) |

Return `4`.

## Key Insights & Edge Cases

- **A first `1` always exists.** The array is infinite and eventually all `1`s,
  so the gallop cannot run forever — no artificial cap or "not found" sentinel is
  needed (contrast with a *finite* array, where you would also need a valid `hi`
  and a `-1` fallback).
- **First element is `1` (transition at 0):** `get(1)` may be `1`, ending the
  gallop at `bound = 1`; the window `[0, 1]` binary search finds `1` at index
  `0`. If `get(1)` were `0`, index 0 must be `0` too, so `bound = 1` still gives
  the right window.
- **Leftmost, not any.** A plain "found a 1, return mid" search would return an
  arbitrary `1`. The `hi = mid - 1` branch after recording `ans` is what pins
  the *first* `1`.
- **Monotonic-predicate framing generalizes.** Replace "`get(i) == 1`" with any
  predicate that flips once from false to true (e.g. "`arr[i] >= target`") and
  the same gallop-then-bisect skeleton finds the boundary — this is the bridge
  to lower-bound / first-occurrence searches (Problem 4).
- **Careful with a *finite* variant.** If the array were finite and padded with
  a "`0`" out-of-bounds sentinel, doubling could leap over a short block of `1`s
  at the very end and you could never distinguish real `0`s from past-the-end.
  The clean, well-posed version — and the one asked here — is the truly infinite
  array whose tail is all `1`s.
