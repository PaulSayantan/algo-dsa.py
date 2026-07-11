# Solution — Squares Starting at Each Index

## Brute Force

For each index `i`, try every block length and count matches.

```python
def squares_per_start_index_brute(s):
    n = len(s); ans = [0]*n
    for i in range(n):
        for L in range(1, (n - i) // 2 + 1):
            if s[i:i+L] == s[i+L:i+2*L]:
                ans[i] += 1
    return ans
```

- **Time:** O(n³) naive, O(n²) with hashing.
- **Space:** O(n) for the output.

At `n = 2·10⁵` the O(n²) inner work is far too slow, and simply writing one `+1` per
square is Θ(n²) on inputs like `"aaaa...a"`.

## Optimal Approach — Main–Lorentz Algorithm + Difference Array

Main–Lorentz emits squares as **O(n log n) ranges**:

> `(lo, hi, l)` = "every start index in `[lo, hi]` begins a square of length `2l`."

Each range contributes exactly `+1` to `ans[p]` for every `p` in `[lo, hi]`. Adding
`+1` to a whole contiguous interval is the textbook job for a **difference array**:

```python
diff[lo]  += 1
diff[hi+1] -= 1
```

After processing all O(n log n) ranges, a single prefix sum over `diff` produces the
final `ans[i]` for every `i` in one pass — turning what looks like Θ(n²) range
updates into O(n log n + n) total work.

### Why it is correct

- Main–Lorentz enumerates every square occurrence exactly once, partitioned into
  disjoint ranges (the `l - 1` cap on the left-centered case prevents a square from
  being emitted twice). So the number of ranges covering index `i` equals the number
  of squares starting at `i`.
- The difference-array identity `ans[i] = sum_{j<=i} diff[j]` correctly reconstructs,
  for each `i`, how many `[lo, hi]` intervals contain `i`.

Validated exhaustively against brute force on all binary strings up to length 11 and
thousands of random ternary strings. On `"mississippi"` it produces
`[0, 1, 2, 0, 0, 1, 0, 0, 1, 0, 0]`, matching the hand-checked squares.

### Complexity

- **Time:** O(n log n) — range construction dominates; difference-array update is
  O(1) per range and the prefix sum is O(n).
- **Space:** O(n) for `diff` and the answer (O(n log n) only if you also store the
  raw ranges).

### Reference implementation

```python
from typing import List

def z_function(s):
    n = len(s); z = [0]*n; l = r = 0
    for i in range(1, n):
        if i < r: z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]: z[i] += 1
        if i + z[i] > r: l, r = i, i + z[i]
    return z

def _gz(z, i): return z[i] if 0 <= i < len(z) else 0

def square_ranges(S):
    out = []
    def rec(s, shift):
        n = len(s)
        if n < 2: return
        nu = n // 2; nv = n - nu
        u, v = s[:nu], s[nu:]
        rec(u, shift); rec(v, shift + nu)
        z1 = z_function(u[::-1])
        z2 = z_function(v + '#' + u)
        z3 = z_function(u[::-1] + '#' + v[::-1])
        z4 = z_function(v)
        for cntr in range(n):
            if cntr < nu:
                l = nu - cntr
                k1 = _gz(z1, nu - cntr); k2 = _gz(z2, nv + 1 + cntr); left = True
            else:
                l = cntr - nu + 1
                k1 = _gz(z3, nu + 1 + nv - 1 - (cntr - nu)); k2 = _gz(z4, (cntr - nu) + 1); left = False
            if k1 + k2 < l: continue
            lo = max(1, l - k2); hi = min(l, k1)
            if left: hi = min(hi, l - 1)
            if lo > hi: continue
            if left:
                s_lo, s_hi = shift + cntr - hi, shift + cntr - lo
            else:
                s_lo, s_hi = shift + cntr - l - hi + 1, shift + cntr - l - lo + 1
            out.append((s_lo, s_hi, l))
    rec(S, 0)
    return out

def squares_per_start_index(s: str) -> List[int]:
    n = len(s)
    diff = [0] * (n + 1)
    for lo, hi, l in square_ranges(s):
        diff[lo] += 1
        diff[hi + 1] -= 1
    ans = [0] * n
    running = 0
    for i in range(n):
        running += diff[i]
        ans[i] = running
    return ans
```

## Key Insights & Edge Cases

- **Difference array turns interval updates into O(1) each** — this is what keeps the
  algorithm at O(n log n) even when the total number of squares is Θ(n²).
- **Index bounds:** `diff` has size `n + 1` so that `diff[hi + 1]` is always valid
  when `hi == n - 1`.
- **`aaaa` → `[2, 1, 1, 0]`:** index 0 gets both `"aa"` (L=1) and `"aaaa"` (L=2).
- **Square-free strings** yield an all-zeros array.
- If you want per-index counts of *distinct lengths only*, that is the same as this
  (each range fixes one length `2l`), but per-index *distinct content* would need
  extra hashing as in Problem 4.
