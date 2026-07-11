# Solution — Detect a Tandem Repeat

## Brute Force

Try every start index `i` and every block length `L`, and check whether
`s[i:i+L] == s[i+L:i+2L]`.

```python
def contains_tandem_repeat_brute(s: str) -> bool:
    n = len(s)
    for i in range(n):
        for L in range(1, (n - i) // 2 + 1):
            if s[i:i+L] == s[i+L:i+2*L]:
                return True
    return False
```

- There are O(n²) `(i, L)` pairs, and each comparison costs up to O(n).
- **Time:** O(n³) naively, O(n²) if you compare with hashing / Z-function.
- **Space:** O(1) extra (or O(n) with hashing).

Fine for `n` up to a few thousand, too slow at `n = 2·10⁵`.

## Optimal Approach — Main–Lorentz Algorithm

**Key definition.** A *square* is a substring `XX`. Let `2l` be its length, so
`l = |X|` is the *half length*.

**Divide.** Split `s` into `u = s[:n//2]` and `v = s[n//2:]`. Every square either

1. lies entirely inside `u`,
2. lies entirely inside `v`, or
3. **crosses** the boundary between `u` and `v`.

Cases (1) and (2) are handled by recursing on `u` and `v`. Only case (3) needs new
work at this level.

**Conquer (crossing squares).** Classify a crossing square by whether its **center**
(the boundary between its two halves `X|X`) falls in the left half or the right half:

- *Left-centered* squares: the center lies inside `u`. For a center position and a
  half length `l`, the square exists iff
  - the block extends far enough to the **right** into `v` and the tail of `u`, and
  - it extends far enough to the **left** inside `u`.
- *Right-centered* squares are the mirror image, handled symmetrically on `v`.

The two extension lengths are read off from **Z-functions**:

- `z1 = Z(reverse(u))` — how far a suffix of `u` matches backward.
- `z2 = Z(v + '#' + u)` — how far `v` matches into `u` going forward.
- `z3 = Z(reverse(u) + '#' + reverse(v))` — mirror of `z2`.
- `z4 = Z(v)` — internal matches of `v`.

For each center, we obtain a left reach `k1` and a right reach `k2`. A square of
half length `l` exists at that center **iff `k1 + k2 >= l`**, and in fact an entire
contiguous *range* of valid start positions exists at once.

**For detection specifically** we do not even need the exact range: the moment we
find a center where `k1 + k2 >= l` (with a valid, non-empty start range), we can
return `True`. Otherwise, after both halves report `False` and no crossing exists,
the string is square-free.

### Why it is correct

Every square is either fully inside a half (found by recursion) or crosses the
midpoint (found by the Z-based scan). The Z-function values give, exactly, the
longest match extending left/right from the boundary, so `k1 + k2 >= l` is a
necessary and sufficient condition for a crossing square of half length `l` to
exist at that center. No square is missed and none is falsely reported.

### Complexity

- Each recursion level does O(n) Z-function work; there are O(log n) levels.
- **Time:** O(n log n).
- **Space:** O(n) for the Z-arrays (rebuilt per level).

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

def contains_tandem_repeat(s: str) -> bool:
    found = [False]
    def rec(t):
        n = len(t)
        if n < 2 or found[0]: return
        nu = n // 2; nv = n - nu
        u, v = t[:nu], t[nu:]
        rec(u); rec(v)
        if found[0]: return
        z1 = z_function(u[::-1])
        z2 = z_function(v + '#' + u)
        z3 = z_function(u[::-1] + '#' + v[::-1])
        z4 = z_function(v)
        for cntr in range(n):
            if cntr < nu:
                l = nu - cntr
                k1 = _gz(z1, nu - cntr); k2 = _gz(z2, nv + 1 + cntr)
                left = True
            else:
                l = cntr - nu + 1
                k1 = _gz(z3, nu + 1 + nv - 1 - (cntr - nu)); k2 = _gz(z4, (cntr - nu) + 1)
                left = False
            if k1 + k2 < l: continue
            lo = max(1, l - k2); hi = min(l, k1)
            if left: hi = min(hi, l - 1)   # exclude the degenerate l1 == l case
            if lo <= hi:
                found[0] = True; return
    rec(s)
    return found[0]
```

## Key Insights & Edge Cases

- **A single character is not a square.** The base case `n < 2` returns without
  reporting, and the `l - 1` cap on the left case prevents a zero-length block.
- **Empty string** (if allowed) has no square → `False`.
- **All-equal strings** like `"aaaa"` are heavy with squares; detection returns on
  the very first crossing found, so it stays fast.
- The condition `k1 + k2 >= l` is the single most important invariant — memorize it.
- If you only need *existence*, you can early-exit as soon as one range is found,
  which is what the `found` flag above does.
