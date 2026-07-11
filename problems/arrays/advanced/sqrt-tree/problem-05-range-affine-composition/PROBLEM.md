# Range Affine (Linear Function) Composition

**Difficulty:** Hard

**Source:** Classic (AtCoder Library Practice Contest "Point Set Range Composite", ABL-E family) — static-query variant

## Description

You are given `n` linear functions, indexed `0..n-1`. Function `i` is
`f_i(x) = a_i · x + b_i`, represented by the pair `(a_i, b_i)`. All arithmetic is done
**modulo** `M = 1_000_000_007`.

Answer `q` queries. Each query gives `l`, `r`, and a value `x`, and asks for the result of
composing the functions from index `l` through `r` (outer to inner, `l` outermost) applied
to `x`:

```
f_l( f_{l+1}( ... f_r(x) ... ) )   (mod M)
```

Equivalently, the composed function `F = f_l ∘ f_{l+1} ∘ ... ∘ f_r` is itself affine,
`F(x) = A·x + B`; return `F(x) mod M`.

Preprocess once, answer each query in **O(1)**.

Function composition is **associative** but **NOT commutative** (`f∘g != g∘f` in general)
and **NOT invertible in a way usable for prefix arrays** — so, as with product-mod, neither
prefix combination nor a sparse table applies:

- **Prefix arrays fail:** there is no general "un-compose" that peels a prefix off a composed
  affine map without computing modular inverses of the `a` coefficients, which may be `0` or
  non-invertible.
- **Sparse tables fail:** composition is not idempotent, so overlapping ranges would apply
  the overlapped functions twice.
- **Order matters:** the combine must preserve left-to-right order, which the Sqrt Tree does.

Represent each element as the pair `(a_i, b_i)` and combine with the affine-composition
operator. Implement `RangeAffine` with a constructor taking the list of `(a, b)` pairs and
`query(l, r, x)`.

## Constraints

- `1 <= n <= 10^5`
- `0 <= a_i, b_i < M` where `M = 1_000_000_007`
- `1 <= q <= 10^5`
- `0 <= l <= r < n`, `0 <= x < M`

## Composition rule

If `g(x) = a1·x + b1` (outer) and `h(x) = a2·x + b2` (inner), then
`(g ∘ h)(x) = a1·(a2·x + b2) + b1 = (a1·a2)·x + (a1·b2 + b1)`, i.e.

```
op((a1, b1), (a2, b2)) = ( a1·a2 mod M ,  (a1·b2 + b1) mod M )
```

Note `op` is **not** symmetric in its two arguments — order matters.

## Examples

### Example 1

```
Input:
  funcs = [(2, 3), (1, 5), (3, 0), (2, 1)]   # (a_i, b_i)
  query(1, 2, x=2)

Output:
  11

Explanation:
  Compose f_1 ∘ f_2 applied to 2, innermost first:
    f_2(2) = 3*2 + 0 = 6
    f_1(6) = 1*6 + 5 = 11
  Result = 11.
```

### Example 2

```
Input:
  funcs = [(2, 3), (1, 5), (3, 0), (2, 1)]
  query(0, 3, x=1)

Output:
  31

Explanation:
  Apply innermost to outermost:
    f_3(1) = 2*1 + 1 = 3
    f_2(3) = 3*3 + 0 = 9
    f_1(9) = 1*9 + 5 = 14
    f_0(14) = 2*14 + 3 = 31
  Result = 31.
```

## Hint

The composition of affine maps is itself an affine map, and composition is associative but
order-sensitive. Split into `√n` blocks; precompute each block's prefix composition, suffix
composition, and the composition over every pair of whole blocks — always combining outer
(smaller index) with inner (larger index). Answer a query by composing suffix ∘ between ∘
prefix, then evaluate at `x`. Build a **Sqrt Tree** whose elements are `(a, b)` pairs and
whose `op` is affine composition.
