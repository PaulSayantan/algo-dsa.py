# Solution — Longest Tandem Repeat

## Brute Force

Check every `(start, half-length)` pair and keep the longest square found.

```python
def longest_tandem_repeat_brute(s: str) -> str:
    n = len(s); best = ""
    for i in range(n):
        for L in range(1, (n - i) // 2 + 1):
            if s[i:i+L] == s[i+L:i+2*L] and 2*L > len(best):
                best = s[i:i+2*L]
    return best
```

- **Time:** O(n²) comparisons × O(n) each = O(n³), or O(n²) with hashing.
- **Space:** O(1) extra (plus the answer).

Because it scans block lengths from small to large, remember to keep the *first*
maximum-length square you meet if you want the leftmost tie-break; the version
above already does, since it only replaces when strictly longer.

## Optimal Approach — Main–Lorentz Algorithm

The insight is that Main–Lorentz gives us **all** squares, but in a *compressed*
form. Instead of listing individual squares (of which there may be Θ(n²)), it emits
**O(n log n) ranges**, each of the form:

> "Every start index `p` in `[lo, hi]` begins a square of length `2l`."

Build this list with the standard divide-and-conquer + Z-function machinery
(`square_ranges` below). Then the longest square is simply the range with the
maximum half length `l`; ties are broken by the smallest `lo` (each range is a
contiguous run of start indices, so the leftmost start within the best `l` is a
range's `lo`).

### Building the ranges

1. Split `s = u + v`. Recurse into `u` and `v`.
2. For crossing squares, compute the four Z-functions
   `z1 = Z(reverse(u))`, `z2 = Z(v + '#' + u)`,
   `z3 = Z(reverse(u) + '#' + reverse(v))`, `z4 = Z(v)`.
3. For each center, get the left reach `k1` and right reach `k2`. If
   `k1 + k2 >= l`, the valid block lengths `l1` form an interval, which maps to a
   contiguous interval of start indices `[s_lo, s_hi]` — record `(s_lo, s_hi, l)`.

### Selecting the answer

```python
best_l, best_start = 0, -1
for lo, hi, l in square_ranges(s):
    if l > best_l or (l == best_l and lo < best_start):
        best_l, best_start = l, lo
return "" if best_l == 0 else s[best_start:best_start + 2*best_l]
```

Within one range every start has the *same* length `2l`, so the smallest start in
the best range (`lo`) is automatically the leftmost among that range's ties.

### Why it is correct

Main–Lorentz provably enumerates every square exactly once across all ranges
(each square is either fully inside a half or crosses exactly one midpoint at some
recursion level). The Z-values compute exact left/right reaches, so
`k1 + k2 >= l` characterizes valid squares and the derived `[s_lo, s_hi]` is
exactly the set of valid start indices. Taking the max `l` and min start therefore
returns the true leftmost-longest square.

### Complexity

- **Time:** O(n log n) to build ranges + O(#ranges) = O(n log n) to scan.
- **Space:** O(n log n) if you materialize the ranges, or O(n) if you fold the max
  computation directly into the recursion.

### Reference implementation

```python
def z_function(s):
    n = len(s); z = [0]*n; l = r = 0
    for i in range(1, n):
        if i < r: z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]: z[i] += 1
        if i + z[i] > r: l, r = i, i + z[i]
    return z

def _gz(z, i): return z[i] if 0 <= i < len(z) else 0

def square_ranges(S):
    """Yield (start_lo, start_hi, l): every start in [start_lo, start_hi] begins
    a square of length 2*l.  Total O(n log n) ranges."""
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

def longest_tandem_repeat(s: str) -> str:
    best_l, best_start = 0, -1
    for lo, hi, l in square_ranges(s):
        if l > best_l or (l == best_l and lo < best_start):
            best_l, best_start = l, lo
    return "" if best_l == 0 else s[best_start:best_start + 2*best_l]
```

## Key Insights & Edge Cases

- **Compression is the whole point.** For `"aaaa...a"` there are Θ(n²) squares but
  only O(n log n) ranges, so never materialize the squares one by one.
- **Tie-breaking** is subtle: the leftmost longest square is `min lo` over the
  ranges with maximal `l`. Do not compare full substrings — compare `(l, lo)`.
- **Square-free input** returns `""`; guard `best_l == 0`.
- **Odd/even lengths:** the answer length `2·best_l` is always even by definition.
- The `left`-case cap `hi = min(hi, l - 1)` excludes the degenerate block that
  would double-count a right-centered square, keeping each square in exactly one
  range.
