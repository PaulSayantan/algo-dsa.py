# Solution — Iahub and Xors

## Brute Force

Store the matrix. Each update/query loops over its submatrix.

- **Time:** `O(m · n²)` — `10^5 · 10^6 = 10^11`. Far too slow.
- **Space:** `O(n²)`.

## Optimal Approach — 2D BIT, range-update / range-query, XOR flavor

This combines everything: **range updates *and* range queries**, the hardest BIT
mode. The 1D template uses the difference trick plus extra BITs to reconstruct
the sum; here we adapt it to XOR, which is its own inverse.

### XOR difference decomposition

Define a difference matrix `d` so that each cell is a prefix-XOR of `d`:

```
a[x][y] = XOR of d[p][q] over all p <= x, q <= y.
```

Then XORing `v` into the rectangle `[x0..x1] × [y0..y1]` is **four corner
stamps** — the XOR analogue of the `+ - - +` sum stamps, except XOR is self-
inverse so every corner is simply `^= v`:

```
d[x0][y0]     ^= v
d[x1+1][y0]   ^= v
d[x0][y1+1]   ^= v
d[x1+1][y1+1] ^= v
```

(A cell inside the rectangle sees exactly one corner `<= (x,y)` → v applied once;
a cell past an edge sees two corners → they cancel. Same combinatorics as the sum
difference array, with parity replacing signed cancellation.)

### The key XOR-parity insight

We need `P(x, y) = XOR of a[i][j] over i <= x, j <= y`. Substituting the
decomposition, `d[p][q]` is XORed into `P(x,y)` once for every `(i,j)` with
`p <= i <= x` and `q <= j <= y` — that is `(x - p + 1) · (y - q + 1)` times.
Because XOR cancels in pairs, **`d[p][q]` survives iff that product is odd**,
which happens iff **both** factors are odd:

```
(x - p + 1) odd  AND  (y - q + 1) odd
  <=>  p ≡ x (mod 2)  AND  q ≡ y (mod 2).
```

So the prefix XOR at `(x, y)` depends only on the `d[p][q]` sharing `x`'s row
parity and `y`'s column parity:

```
P(x, y) = XOR of d[p][q] over p <= x, q <= y  with  p ≡ x, q ≡ y (mod 2).
```

### Four BITs keyed by parity

Keep four Fenwick trees, one per bucket `(x & 1, y & 1)`.

- `_point_xor(x, y, v)`: XOR `v` into bucket `(x & 1, y & 1)` via the usual 2D
  Fenwick ascent on `x, y`. Every entry in a bucket therefore shares that
  bucket's parity.
- `_prefix_xor(x, y)`: select the single bucket `(x & 1, y & 1)` and take its 2D
  Fenwick prefix XOR up to `(x, y)`. Since the bucket only holds correctly-parity
  entries, this returns exactly the parity-filtered XOR above — no parity checks
  are needed during traversal.

```
def _point_xor(self, x, y, v):
    b = self.bit[(x & 1)][(y & 1)]
    i = x
    while i <= n:
        j = y
        while j <= n:
            b[i][j] ^= v
            j += j & (-j)
        i += i & (-i)

def _prefix_xor(self, x, y):
    b = self.bit[(x & 1)][(y & 1)]
    res, i = 0, x
    while i > 0:
        j = y
        while j > 0:
            res ^= b[i][j]
            j -= j & (-j)
        i -= i & (-i)
    return res
```

### Query via inclusion–exclusion (signs disappear)

```
submatrix_xor(x0,y0,x1,y1)
   = P(x1, y1) ^ P(x0-1, y1) ^ P(x1, y0-1) ^ P(x0-1, y0-1)
```

With XOR there is no subtraction — the four prefix XORs are simply XORed, and the
double-counted overlaps cancel themselves.

### Worked check (Example 1)

Matrix after the three updates:
```
1 1 2
1 1 2
3 3 3
```
- `1 2 2 3 3` → `1 ^ 2 ^ 3 ^ 3 = 3`. ✔
- `1 2 2 3 2` → `1 ^ 3 = 2`. ✔

- **Time:** `O((n² + m) · log²n)`; each op is `O(log²n)`.
- **Space:** `O(n²)` (four `(n+1)×(n+1)` BITs).

## Key Insights & Edge Cases

- **XOR is self-inverse**, which is exactly why a Fenwick-style structure works
  for range-update/range-query here: the "difference" and the inclusion–exclusion
  both collapse to plain XORs with no signs.
- **The parity buckets are the crux.** A single BIT would XOR each `d[p][q]` into
  every prefix regardless of parity, corrupting the answer. Four buckets keyed by
  `(x&1, y&1)` isolate exactly the survivors. (This mirrors the four *summing*
  BITs of the classic range-update/range-query sum problem, but the reason is
  parity of an inclusion count, not `i·j` coefficients.)
- **Corner stamps can hit `n+1`** (`x1+1`, `y1+1`). Size each BIT to `n+1` (index
  up to `n+1`) or guard the ascent so those stamps don't overflow — they still
  matter for cells at the boundary.
- **Even multiplicity cancels:** Example 2's full-matrix query XORs `5` four times
  → `0`. The structure reproduces this automatically.
- **Values up to `2^62`** fit in Python ints natively; in C++ use `long long`.
- **1-indexing is mandatory** for Fenwick; the problem is already 1-indexed, and
  `x0-1 = 0` cleanly maps to the empty prefix.
