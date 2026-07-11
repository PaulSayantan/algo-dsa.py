# Solution — Range Affine Composition

## Brute Force

For each query, apply the functions from `r` down to `l` (innermost first).

```python
MOD = 1_000_000_007
def query(funcs, l, r, x):
    res = x
    for i in range(r, l - 1, -1):        # innermost (r) first
        a, b = funcs[i]
        res = (a * res + b) % MOD
    return res
```

- **Time:** O(n) per query, O(q·n) total.
- **Space:** O(1) extra.

### Why prefix arrays and sparse tables fail

- **Composition is not commutative.** `f∘g != g∘f`, so any structure must combine pieces in
  the correct **left-to-right (outer-to-inner)** order.
- **Not invertible for prefixes.** To "peel" a prefix of a composed affine map you would need
  the modular inverse of the accumulated `a` coefficient. That coefficient can be `0` or share
  a factor with `MOD`... actually `MOD` is prime here, but a single `a_i = 0` collapses the
  composite `A` to `0`, which has no inverse — so prefix un-composition still breaks in
  general. Prefix arrays are not a reliable route.
- **Not idempotent.** A sparse table overlaps its two covering ranges; applying the overlapped
  functions twice changes the result.

## Optimal Approach (Sqrt Tree)

Composition of affine maps is **closed** (the composite is affine) and **associative**:
`(f∘g)∘h = f∘(g∘h)`. Store each element as the pair `(a, b)`, use

```
op((a1, b1), (a2, b2)) = ( a1*a2 mod M , (a1*b2 + b1) mod M )    # first arg = outer
```

and build the generic Sqrt Tree over these pairs. Per layer we keep the prefix composition,
suffix composition, and the between-blocks composition — every combine placing the
smaller-index (outer) operand on the left. A query composes at most three stored maps
(`suf[l]`, `between[bl..br]`, `pref[r]`, in that order) into a single `(A, B)`, then returns
`(A·x + B) mod M`.

### Why it is correct

The three pieces cover `[l, r]` as **disjoint, ordered** segments: the suffix of `l`'s block
(indices `l..blockEnd`), the whole blocks strictly between, and the prefix of `r`'s block
(indices `blockStart..r`). Composing them left-to-right reconstructs
`f_l ∘ f_{l+1} ∘ ... ∘ f_r` exactly, because associativity lets us regroup the composition
while the fixed left-to-right ordering preserves the (non-commutative) order. Evaluating the
resulting affine map at `x` gives the answer. Elements are never revisited (no idempotence
needed) and never "un-composed" (no invertibility needed).

### Reference implementation (answer key)

```python
MOD = 1_000_000_007

def affine_op(A, B):
    a1, b1 = A
    a2, b2 = B
    return (a1 * a2 % MOD, (a1 * b2 + b1) % MOD)

class RangeAffine(SqrtTree):     # SqrtTree = generic class from problem 1
    def __init__(self, funcs):
        super().__init__(funcs, op=affine_op)

    def query(self, l, r, x):
        a, b = super().query(l, r)   # composed (A, B) over [l, r]
        return (a * x + b) % MOD
```

- **Build:** O(n log log n) composition operations.
- **Query:** O(1) — at most two compositions plus one evaluation.
- **Space:** O(n log log n) pairs.

## Key Insights & Edge Cases

- **Order is everything.** Verify with a two-element range that your `op` is applied
  outer-on-left. For `funcs = [(2,3),(1,5),...]`, `query(0,1,x)` must give
  `f_0(f_1(x)) = 2·(1·x + 5) + 3 = 2x + 13`, not `f_1(f_0(x)) = 1·(2x + 3) + 5 = 2x + 8`.
- **Identity element** for composition is `(1, 0)` (i.e. `f(x) = x`); useful if you seed
  accumulators, though the prefix/suffix formulation seeds with the first/last element and
  needs no identity.
- **`a_i = 0`** is allowed and simply makes that function constant; the structure handles it.
- **Point-update variant:** if functions can change, use the **updatable Sqrt Tree** (O(√n)
  update, still O(1) query) — this is exactly ACL's "Point Set Range Composite" with an added
  O(1)-query requirement. A segment tree gives O(log n) query with O(log n) update instead.
- This problem generalizes to **matrix products** over a range (same associative,
  non-commutative structure), another canonical Sqrt Tree application.
