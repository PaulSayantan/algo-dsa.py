# Discrete Logarithm (Baby-Step Giant-Step) — Solution

## Brute Force

Scan exponents `0, 1, 2, ...` computing `a^x mod m` incrementally.

```python
def discrete_log(a, b, m):
    a %= m; b %= m
    cur = 1 % m               # a^0
    for x in range(m):        # by Fermat, order divides m-1 < m
        if cur == b:
            return x
        cur = (cur * a) % m
    return -1
```

- **Time:** `O(m)` — up to `10^9` multiplications, too slow.
- **Space:** `O(1)`.

## Optimal Approach (Baby-Step Giant-Step = Meet in the Middle)

Let `n = ceil(sqrt(m))`. Any exponent `x` in `[0, m)` can be written as

```
x = i * n - j,   where 1 <= i <= n  and  0 <= j < n.
```

(Equivalently the classic `x = i*n + j`; the `i*n - j` form makes the smallest
answer easy to recover.) Substituting into `a^x ≡ b (mod m)`:

```
a^(i*n - j) ≡ b
a^(i*n)     ≡ b * a^j      (multiply both sides by a^j)
(a^n)^i     ≡ b * a^j      (mod m)
```

The left side depends only on `i` (the **giant steps**, each advancing by a
factor `a^n`); the right side depends only on `j` (the **baby steps**). We
enumerate each half independently and match — exactly Meet in the Middle, with
the two "halves" being the high and low parts of the exponent.

**Step by step**

1. `a %= m`, `b %= m`. Handle the tiny edge case `b == 1` → `x = 0`.
2. **Baby steps:** for `j = 0 .. n`, compute `b * a^j mod m` and store
   `table[value] = j`. Storing the *largest* `j` per value (later writes
   overwrite) helps yield the minimal `x` after the giant loop.
3. **Giant steps:** let `g = a^n mod m`. For `i = 1 .. n`, compute
   `cur = g^i mod m` (incrementally: `cur = cur * g`). If `cur` is a key in
   `table`, then `x = i*n - table[cur]` is a solution.
4. Track the minimum valid `x` over all collisions (or return the first, which
   with the `i` loop increasing and appropriate `j` bookkeeping is the
   smallest). Return `-1` if no collision ever occurs.

```python
from math import isqrt

def discrete_log(a, b, m):
    a %= m; b %= m
    n = isqrt(m) + 1                       # ceil(sqrt(m))

    # Baby steps: value -> j  (keep the largest j for a given value)
    table = {}
    cur = b % m
    for j in range(n + 1):
        table[cur] = j
        cur = (cur * a) % m

    # Giant steps: (a^n)^i
    an = pow(a, n, m)
    cur = 1
    best = -1
    for i in range(1, n + 1):
        cur = (cur * an) % m               # cur = a^(i*n)
        if cur in table:
            x = i * n - table[cur]
            if x >= 0:
                best = x
                break                      # first hit with smallest i, largest j
    return best
```

Why it is correct: as `(i, j)` ranges over `1 <= i <= n`, `0 <= j <= n`, the
value `i*n - j` covers every integer in `[0, m)` (since `n^2 >= m`). So if a
solution exists it is representable, and the equation `(a^n)^i ≡ b*a^j`
holds iff `a^(i*n - j) ≡ b`. Scanning `i` in increasing order and, per value,
keeping the largest `j` yields the smallest exponent at the first collision.

- **Time:** `O(sqrt(m))` — `n ≈ sqrt(m)` baby steps to build the table and
  `n` giant steps, each `O(1)` amortized (hash lookup + one multiply). For
  `m = 10^9`, `sqrt(m) ≈ 31623` — trivial.
- **Space:** `O(sqrt(m))` for the baby-step hash table.

## Key Insights & Edge Cases

- **The exponent is the thing being split**, not an array. Writing
  `x = i*n - j` (or `i*n + j`) is the MITM move: the base `a` is exponentiated
  in two independent "strides," and a hash map glues them together. This is the
  same halving-the-search idea as the subset problems, applied to a multiplicative
  group.
- **`b == 1` → answer 0**; the baby-step seed `cur = b` and giant loop starting
  at `i = 1` mean you should special-case (or verify) `x = 0` up front.
- **Prime modulus assumption:** with `m` prime, `gcd(a, m) = 1`, so `a` is
  invertible and the `i*n - j` derivation is valid. For non-prime `m` the
  algorithm needs a generalization (factor out `gcd`s) — out of scope here.
- **Choosing `n = ceil(sqrt(m))`** balances the two halves (`sqrt(m)` baby
  steps vs `sqrt(m)` giant steps), the same "balance the split" principle that
  minimizes total work in every MITM problem.
- **Return smallest `x`:** iterate giant steps with increasing `i` and, in the
  baby table, prefer the largest `j` for each residue so that the first
  collision gives the minimum non-negative exponent.
