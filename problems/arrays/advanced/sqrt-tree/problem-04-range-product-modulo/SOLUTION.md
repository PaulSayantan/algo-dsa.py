# Solution — Range Product Modulo m

## Brute Force

Multiply `l..r` mod `m` per query.

```python
def query(nums, m, l, r):
    p = 1
    for i in range(l, r + 1):
        p = (p * nums[i]) % m
    return p
```

- **Time:** O(n) per query, O(q·n) total.
- **Space:** O(1) extra.

### Why the usual O(1) tricks do NOT work here

- **Prefix products + modular inverse:** `product(l..r) = prefix[r] · prefix[l-1]^{-1} mod m`.
  The inverse `prefix[l-1]^{-1}` exists **only** when `gcd(prefix[l-1], m) = 1`. With `m`
  composite or with elements sharing a factor of `m`, that gcd is often `> 1` and no inverse
  exists. Concretely, for `nums = [3,7,4,9,6,2]`, `m = 100`, the prefix products mod 100 are
  `[1, 3, 21, 84, 56, 36, 72]`; `prefix[3] = 56` has `gcd(56, 100) = 4`, so you cannot divide
  it out to recover `query(1, 3) = 52`. **Prefix products are impossible.**
- **Sparse table:** answers a range as `op(table[l][k], table[r-2^k+1][k])` with the two
  halves **overlapping**. That is correct only if `op` is idempotent. Multiplication mod `m`
  is not (`x·x mod m != x`), so the overlapped region is multiplied twice → wrong. **Sparse
  table is impossible.**

## Optimal Approach (Sqrt Tree)

Multiplication mod `m` **is associative**: `((a·b)·c) mod m = (a·(b·c)) mod m`. Associativity
is the *only* property the Sqrt Tree needs, because it partitions `[l, r]` into **disjoint,
contiguous** pieces (never overlapping, never dividing).

Build the generic Sqrt Tree with `op = lambda x, y: (x * y) % m`. Per layer store prefix
products, suffix products, and the between-blocks products, all mod `m`. A query is:

```
answer = suf[layer][l]                         # product from l to end of its block
if inner whole blocks exist:
    answer = (answer * between[layer][bl..br]) % m
answer = (answer * pref[layer][r]) % m         # product from start of r's block to r
```

with base cases `l == r` → `nums[l]` and `l + 1 == r` → `nums[l]·nums[r] mod m`.

### Why it is correct

The three pieces (suffix of `l`'s block, whole blocks strictly between, prefix of `r`'s
block) are disjoint and their concatenation, in order, is exactly `nums[l..r]`. Because
multiplication is associative we may multiply the three precomputed partial products in that
order and reduce mod `m` at each step; the result equals the full product mod `m`. Since we
never revisit an element, non-idempotence is irrelevant; since we never divide,
non-invertibility is irrelevant.

### Reference implementation (answer key)

Reuse the generic Sqrt Tree from Problem 1, binding `m`:

```python
class RangeProductMod(SqrtTree):     # SqrtTree = generic class from problem 1
    def __init__(self, nums, mod):
        self.mod = mod
        super().__init__(nums, op=lambda x, y: (x * y) % mod)
```

- **Build:** O(n log log n) modular multiplications.
- **Query:** O(1) (exactly two multiplications and mods beyond the lookups).
- **Space:** O(n log log n).

## Key Insights & Edge Cases

- **Zeros:** if any element in `[l, r]` is `0` (or `≡ 0 mod m`), the product is `0`. The
  Sqrt Tree handles this naturally — and note this is *also* a case prefix products choke on
  (a zero prefix has no inverse). This is the crux of the problem.
- **m not prime / shared factors:** the entire point — no modular inverse, so no prefix trick.
- **Empty product / single element:** `query(i, i)` returns `nums[i] mod m` via the base case.
- **Reduce inputs first:** ensure `0 <= nums[i] < m` so intermediate products stay below
  `m^2` (fits in 64-bit when `m <= 1e9`; Python integers are unbounded anyway).
- This problem, together with Problem 5, is the reason Sqrt Tree exists: **O(1) queries for
  an associative operation that is neither invertible nor idempotent.**
