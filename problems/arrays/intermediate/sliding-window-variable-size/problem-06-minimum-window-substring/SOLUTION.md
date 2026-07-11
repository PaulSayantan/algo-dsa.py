# Solution — Minimum Window Substring

## Brute Force

Enumerate every substring `s[l..r]` and check whether it covers the multiset of
`t`; keep the shortest that does.

```python
from collections import Counter

def minWindow(s, t):
    need = Counter(t)
    n = len(s)
    best = ""
    for l in range(n):
        for r in range(l, n):
            window = Counter(s[l:r + 1])
            if all(window[c] >= need[c] for c in need):
                if best == "" or (r - l + 1) < len(best):
                    best = s[l:r + 1]
                break  # no need to extend r further from this l
    return best
```

- **Time:** `O(n^2 * A)` (or worse) where `A` is the alphabet size for the cover
  check — far too slow for `n = 10^5`.
- **Space:** `O(A)`.

## Optimal Approach (Sliding Window, variable size)

This is the **shortest-covering-window** flavor. We track how many of `t`'s
*required* character occurrences are currently satisfied by the window and use a
single counter `formed` to decide validity in `O(1)`.

**State:**

- `need`: a `Counter` of `t` — how many of each character we require.
- `window`: counts of each character currently in the window.
- `required = len(need)`: number of *distinct* characters we must satisfy.
- `formed`: number of distinct characters whose window count has reached its
  required count. The window **covers** `t` exactly when `formed == required`.

**Algorithm:**

1. For each `right`, add `c = s[right]` to `window`. If `c` is needed and
   `window[c]` just reached `need[c]`, increment `formed`.
2. **While** `formed == required` (window is valid), it covers `t`:
   - Record the window `[left, right]` if it is the smallest so far.
   - Remove `s[left]` from `window`; if `s[left]` is needed and its count drops
     *below* `need[s[left]]`, decrement `formed` (window no longer valid).
   - Advance `left`.
3. Return the best window recorded (or `""` if none).

```python
from collections import Counter

def minWindow(s, t):
    if not s or not t or len(t) > len(s):
        return ""
    need = Counter(t)
    required = len(need)
    window = {}
    formed = 0
    left = 0
    best_len = float("inf")
    best_l = 0
    for right, c in enumerate(s):
        window[c] = window.get(c, 0) + 1
        if c in need and window[c] == need[c]:
            formed += 1
        while formed == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_l = left
            lc = s[left]
            window[lc] -= 1
            if lc in need and window[lc] < need[lc]:
                formed -= 1
            left += 1
    return "" if best_len == float("inf") else s[best_l:best_l + best_len]
```

**Why it is correct.** The window covers `t` iff for every required character `x`,
`window[x] >= need[x]`. The `formed` counter compresses that whole check into one
integer: it counts exactly the distinct required characters currently satisfied,
so `formed == required` is equivalent to full coverage. Whenever the window is
valid we shrink maximally — dropping left characters until coverage would break —
so for each `right` we find the shortest valid window ending there, and the global
minimum over all `right` is the answer. Both pointers only move forward, giving
linear time.

**Trace of Example 1** (`s = "ADOBECODEBANC"`, `t = "ABC"`, `required = 3`):

- Expand until `right = 5` (`"ADOBEC"`): now A, B, C are all present, `formed = 3`.
  Record length 6. Shrink: `left` advances past `A`, `D`, `O` (none needed until
  `A` leaves) — dropping `A` at index 0 breaks coverage, so the window settles as
  `"DOBEC"`... coverage lost after removing `A`; `formed = 2`.
- Continue expanding. At `right = 10` (`...BA`) coverage returns with window
  `"ODEBANC"`-region; shrinking yields `"BANC"` region reductions.
- The smallest valid window found is `"BANC"` (indices 9..12), length 4.

Result: `"BANC"`.

- **Time:** `O(m + n)` — building `need` is `O(n)`; each of `s`'s characters is
  added once and removed at most once.
- **Space:** `O(A)` for the two counters, where `A` is the alphabet size.

## Key Insights & Edge Cases

- **`formed`/`required` trick** is the crux: it avoids re-scanning the whole
  `need` map on every step, keeping the validity test `O(1)`.
- Compare `window[c] == need[c]` (exactly reaching) when incrementing `formed`,
  and `window[lc] < need[lc]` (dropping below) when decrementing — using `>=`/`<=`
  there would miscount.
- **Duplicates in `t` matter:** `t = "AABC"` requires two `A`s; the counts (not
  just presence) drive `need` and `formed`.
- **No valid window:** if `t` has a character absent from `s`, or needs more copies
  than `s` provides, `formed` never reaches `required`; return `""`.
- **`len(t) > len(s)`** can short-circuit to `""` immediately.
- Record the answer by `(best_l, best_len)` rather than slicing inside the loop to
  avoid repeated `O(window)` string copies.
